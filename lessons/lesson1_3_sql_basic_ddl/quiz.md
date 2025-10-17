# Quiz

### Q1: What SQL statement is used to update data in a table?

- A. SELECT
- B. INSERT
- C. UPDATE
- D. DELETE

### Q2: What is the difference between a table and a view?

- A. A table is a virtual copy of the data, while a view is a physical copy of the data.
- B. A table is a physical copy of the data, while a view is a virtual copy of the data.
- C. A table is a query that is run on the fly when you access the table, while a view is a query that is run on the fly when you access the view.
- D. A table is not stored in the database, but the query that defines the table is stored in the database, while a view is a physical copy of the data.

### Q3: In the following SQL statement, what is 'linda.g@example.com'?

```sql
UPDATE lesson.students
SET email = 'linda.g@example.com'
WHERE id = 4;
```

- A. The column to be updated
- B. The new value for the column
- C. The condition for the update
- D. The table to be updated

### Q4: What SQL statement is used to remove a column from a table?

- A. DELETE COLUMN
- B. REMOVE COLUMN
- C. DROP COLUMN
- D. REMOVE TABLE

### Q5: What does the HEADER option in the COPY statement do?

- A. Specifies the header for the CSV file
- B. Specifies whether to include a header row in the CSV file
- C. Specifies the delimiter for the CSV file
- D. Specifies the table to export data from

### Q6: What is the purpose of creating indexes in SQL?

- A. To rename columns
- B. To improve the performance of queries
- C. To add new columns
- D. To remove existing columns

### Q7: What happens if you try to insert a duplicate value into a column with a unique index in SQL?

- A. The insert will succeed
- B. The insert will fail
- C. The duplicate value will be ignored
- D. The duplicate value will overwrite the existing value

### Q8: What does the CHECK constraint do in SQL?

- A. It checks if a column has a default value
- B. It checks if a column has a unique value
- C. It checks if a column has any NULL values
- D. It checks if a column satisfies a certain condition

### Q9: What is the purpose of a foreign key in a SQL table?

- A. To link tables together
- B. To ensure that each row in the table is unique
- C. To specify a default value for a column
- D. To prevent NULL values in a column

### Q10: In the following SQL statement, what does `REFERENCES lesson.teachers(id)` do?

```sql
CREATE TABLE lesson.classes (
  id INTEGER PRIMARY KEY, -- primary key
  name VARCHAR NOT NULL, -- not null
  teacher_id INTEGER REFERENCES lesson.teachers(id) -- foreign key
);
```

- A. It creates a foreign key that references the id column in the teachers table
- B. It creates a primary key that references the id column in the teachers table
- C. It creates a unique constraint that references the id column in the teachers table
- D. It creates a check constraint that references the id column in the teachers table
