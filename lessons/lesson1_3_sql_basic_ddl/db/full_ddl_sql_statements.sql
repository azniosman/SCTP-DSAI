-- Part 2 - Executing SQL DDL statements

-- 2.1 Create schema
CREATE SCHEMA IF NOT EXISTS lesson;

-- 2.2 Create table
CREATE TABLE lesson.users (
  id INTEGER,
  name VARCHAR,
  email VARCHAR
);

-- 2.3 Insert data
INSERT INTO lesson.users (id, name, email)
VALUES (1, 'John Doe', 'john.doe@gmail.com');

INSERT INTO lesson.users (id, name, email)
VALUES (2, 'Jane Doe', 'jane.doe@gmail.com'),
       (3, 'John Smith', 'john.smith@gmail.com');

-- 2.4 Drop table
DROP TABLE lesson.users;

-- Part 3 - Executing SQL DDL statements based on ERD

-- Drop existing tables first (in reverse dependency order)
DROP TABLE IF EXISTS lesson.students;
DROP TABLE IF EXISTS lesson.classes;
DROP TABLE IF EXISTS lesson.teachers;

-- 3.1 Create tables with constraints
CREATE TABLE lesson.teachers (
  id INTEGER PRIMARY KEY, -- primary key
  name VARCHAR NOT NULL, -- not null
  age INTEGER CHECK(age > 18 AND age < 70), -- check
  address VARCHAR,
  phone VARCHAR,
  email VARCHAR CHECK(CONTAINS(email, '@')) -- check
);

CREATE TABLE lesson.classes (
  id INTEGER PRIMARY KEY, -- primary key
  name VARCHAR NOT NULL, -- not null
  teacher_id INTEGER REFERENCES lesson.teachers(id) -- foreign key
);

CREATE TABLE lesson.students (
  id INTEGER PRIMARY KEY,
  name VARCHAR,
  address VARCHAR,
  phone VARCHAR CHECK(LENGTH(phone) = 8),
  email VARCHAR CHECK(CONTAINS(email, '@')),
  class_id INTEGER REFERENCES lesson.classes(id)
);

-- 3.2 Create indexes
-- Create a unique index 'teachers_name_idx' on the column name of table teachers.
CREATE UNIQUE INDEX teachers_name_idx ON lesson.teachers(name);
-- Create index 'students_name_idx' that allows for duplicate values on the column name of table students.
CREATE INDEX students_name_idx ON lesson.students(name);

-- 3.3 Alter tables
-- Drop students table first to remove dependency
DROP TABLE lesson.students;

-- Add column 'start_date' to table classes.
ALTER TABLE lesson.classes ADD COLUMN start_date DATE;

-- Rename column 'name' to 'code' in table classes.
ALTER TABLE lesson.classes RENAME name TO code;

-- Recreate students table after alterations
CREATE TABLE lesson.students (
  id INTEGER PRIMARY KEY,
  name VARCHAR,
  address VARCHAR,
  phone VARCHAR CHECK(LENGTH(phone) = 8),
  email VARCHAR CHECK(CONTAINS(email, '@')),
  class_id INTEGER REFERENCES lesson.classes(id)
);

-- Part 4 - Tables vs Views

-- Drop existing view if it exists
DROP VIEW IF EXISTS lesson.students_view;

-- 4.1 Create view
CREATE VIEW lesson.students_view AS
SELECT id, name, email
FROM lesson.students;

-- Part 5 - Importing / exporting data

-- 5.1 Importing data (example - replace with actual file path)
-- COPY table_name FROM 'file_name.csv' (AUTO_DETECT TRUE);

-- 5.2 Updating data
UPDATE lesson.students
SET email = 'linda.g@example.com'
WHERE id = 4;

-- 5.3 Exporting data (examples - replace with actual file paths)
-- COPY (SELECT * FROM lesson.students) TO 'students_new.csv' WITH (HEADER 1, DELIMITER '|');
-- COPY (SELECT * FROM lesson.students) TO 'students.json';