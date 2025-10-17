# Quiz

### Q1: What is the purpose of out-of-core computation?

- A. To process data that is too small to fit in memory
- B. To process data that is too large to fit in memory
- C. To process data faster than in-memory computation
- D. To reduce memory usage

### Q2: Which of the following is NOT an advantage of Polars over Pandas?

- A. It uses Arrow arrays for better performance
- B. It can leverage multi-threading
- C. It has a more comprehensive set of features than Pandas
- D. It can process data in chunks

### Q3: How can you force the execution of a lazy query in Polars?

- A. Use the `execute` method
- B. Use the `collect` method
- C. Use the `run` method
- D. Use the `lazy` method

### Q4: How can you read a large CSV file in Polars without loading the entire file into memory?

- A. Use the `read_csv` method
- B. Use the `scan_csv` method
- C. Use the `load_csv` method
- D. Use the `stream_csv` method

### Q5: What is the recommended way to handle large datasets in Pandas?

- A. Use the `read_csv` method with `chunksize` parameter
- B. Use the `read_csv` method without any special parameters
- C. Use the `read_csv` method with `nrows` parameter
- D. Pandas is not suitable for handling large datasets

### Q6: Which of the following is NOT a valid parameter for the `read_csv` method in Polars?

- A. `infer_schema_length`
- B. `n_rows`
- C. `chunksize`
- D. `try_parse_dates`

### Q7: What is the advantage of using lazy evaluation in Polars?

- A. It allows for efficient memory usage
- B. It allows for faster execution
- C. It allows for better optimization of the execution plan
- D. All of the above

### Q8: What is the purpose of the `alias` method in Polars?

- A. To rename a column
- B. To create a new column with a new name
- C. To filter the DataFrame based on a condition
- D. To sort the DataFrame by one or more columns

### Q9: Which of the following is NOT a valid data type in Polars?

- A. `Int64`
- B. `Float64`
- C. `Utf8`
- D. `Datetime32`

### Q10: What is the purpose of the `with_columns` method in Polars?

- A. To add new columns to the DataFrame
- B. To remove columns from the DataFrame
- C. To rename columns in the DataFrame
- D. To sort the DataFrame by one or more columns
