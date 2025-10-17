# Quiz

### Q1: How do you create a new Series with the default index and the data `[2.5, 4.0, 5.5, 6.75]`?

- A. `pd.Series([2.5, 4.0, 5.5, 6.75])`
- B. `pd.Series(data=[2.5, 4.0, 5.5, 6.75])`
- C. `pd.Series(values=[2.5, 4.0, 5.5, 6.75])`
- D. `pd.Series(index=[2.5, 4.0, 5.5, 6.75])`

### Q2: How do you drop the columns 'two' and 'four' from a DataFrame named 'data'?

- A. `data.drop(['two', 'four'], axis=0)`
- B. `data.drop(['two', 'four'], axis=1)`
- C. `data.drop('two', 'four', axis=1)`
- D. `data.drop(index=['two', 'four'])`

### Q3: What is the difference between `loc` and `iloc` indexing in Pandas?

- A. `loc` indexing refers to the index label, while `iloc` refers to the position
- B. `loc` indexing refers to the position, while `iloc` refers to the index label
- C. `loc` is used for Series, while `iloc` is used for DataFrames
- D. There is no difference between `loc` and `iloc`

### Q4: How do you apply a function to each column of a DataFrame named 'frame'?

- A. `frame.apply(func)`
- B. `frame.apply(func, axis='columns')`
- C. `frame.applymap(func)`
- D. `frame.map(func)`

### Q5: How do you rank a DataFrame named 'frame' over the columns?

- A. `frame.rank()`
- B. `frame.rank(axis='columns')`
- C. `frame.rank(axis=1)`
- D. Both B and C are correct

### Q6: What is the purpose of the `combine_first` method in Pandas?

- A. To combine two DataFrames by taking values from the first DataFrame when overlapping
- B. To combine two DataFrames by taking values from the second DataFrame when overlapping
- C. To combine two DataFrames by taking the maximum value when overlapping
- D. To combine two DataFrames by taking the minimum value when overlapping

### Q7: How do you return unique values of the index `pd.Index(['a', 'b', 'c', 'a'])`?

- A. `pd.Index(['a', 'b', 'c', 'a']).unique()`
- B. `pd.Index(['a', 'b', 'c', 'a']).drop_duplicates()`
- C. `pd.Index(['a', 'b', 'c', 'a']).uniq()`
- D. `pd.Index(['a', 'b', 'c', 'a']).distinct()`

### Q8: How do you create a new column 'age' in a DataFrame named 'df' with a scalar value of 25?

- A. `df['age'] = 25`
- B. `df.insert('age', 25)`
- C. `df.add('age', 25)`
- D. `df.append('age', 25)`

### Q9: What is the purpose of the `isna` and `notna` functions in Pandas?

- A. To detect missing or null values
- B. To remove missing or null values
- C. To fill missing or null values
- D. To replace missing or null values

### Q10: What is the purpose of the `na_position` parameter in the `sort_values` method?

- A. To specify the position of missing values in the sorted data
- B. To specify the column(s) to sort by
- C. To specify whether to sort in ascending or descending order
- D. To specify the axis to sort along
