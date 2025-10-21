# Quiz

### Q1: How do you remove duplicate rows from a DataFrame based on a subset of columns?

- A. `df.drop_duplicates(subset=columns)`
- B. `df.unique(subset=columns)`
- C. `df.removedups(columns)`
- D. `df.deduplicate(subset=columns)`

### Q2: How do you rename column labels in a DataFrame?

- A. `df.rename(columns=new_names)`
- B. `df.columns = new_names`
- C. `df.relabel(columns=new_names)`
- D. Both A and B are correct.

### Q3: Which method is used to handle outliers by capping them to a maximum or minimum value?

- A. `df[df.abs() > threshold] = np.sign(df) * threshold`
- B. `df.cap(threshold)`
- C. `df.removeoutliers(threshold)`
- D. `df.clip(threshold)`

### Q4: Which method is used to extract groups from a string pattern using regular expressions?

- A. `df.str.extract(pattern)`
- B. `df.str.findall(pattern)`
- C. `df.str.match(pattern)`
- D. `df.str.grep(pattern)`

### Q5: How do you convert a column of strings to categorical data type?

- A. `df['column'] = df['column'].astype('category')`
- B. `df['column'] = pd.Categorical(df['column'])`
- C. `df['column'] = df['column'].category()`
- D. Both A and B are correct.

### Q6: Which method is used to create dummy variables from a categorical column?

- A. `pd.get_dummies(df['column'])`
- B. `df['column'].dummies()`
- C. `df['column'].one_hot_encode()`
- D. `df['column'].indicator_variables()`

### Q7: How do you read a CSV file into a DataFrame without a header row?

- A. `pd.read_csv(file, header=None)`
- B. `pd.read_csv(file, names=column_names)`
- C. `pd.read_csv(file, skiprows=0)`
- D. Both A and B are correct.

### Q8: How do you skip the first and last rows when reading a CSV file?

- A. `pd.read_csv(file, skiprows=[0, -1])`
- B. `pd.read_csv(file, skip_first_row=True, skip_last_row=True)`
- C. `pd.read_csv(file, header=1, footer=1)`
- D. `pd.read_csv(file, skiprows=lambda x: x==0 or x==len(x)-1)`

### Q9: Which method is used to randomly permute the rows of a DataFrame?

- A. `df.shuffle()`
- B. `df.permute()`
- C. `df.sample(frac=1).reset_index(drop=True)`
- D. `df.iloc[np.random.permutation(len(df))]`

### Q10: How do you write only a subset of columns from a DataFrame to a CSV file?

- A. `df[columns].to_csv(file_path)`
- B. `df.to_csv(file_path, columns=columns)`
- C. `df.subset(columns).to_csv(file_path)`
- D. Both A and B are correct.
