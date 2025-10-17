# Quiz

### Q1: What is the output of the following code?

```python
import numpy as np
my_arr = np.arange(1_000_000)
my_list = list(range(1_000_000))
```

- A. An error.
- B. Two lists of numbers from 1 to 1_000_000.
- C. A list and an array of numbers from 1 to 1_000_000.
- D. Two arrays of numbers from 1 to 1_000_000.

### Q2: How do you create a Numpy array with the shape (3,6) filled with zeros?

- A. np.zeros(3,6)
- B. np.zeros((3,6))
- C. np.array(3,6)
- D. np.array((3,6))

### Q3: What does the `astype` method do in Numpy?

- A. It changes the data type of the array.
- B. It checks the data type of the array.
- C. It creates a new array.
- D. It sorts the array.

### Q4: How do you select the first two rows of a 2D array `arr2d`?

- A. arr2d[:2, :]
- B. arr2d[2, :]
- C. arr2d[:, :2]
- D. arr2d[:, 2]

### Q5: What is the result of the following code `arr2d[:, :1]`?

- A. The first column of arr2d.
- B. The first row of arr2d.
- C. The first two columns of arr2d.
- D. The first two rows of arr2d.

### Q6: What is the result of the following code `arr2d[1, 2]`?

- A. The third element of the second row of arr2d.
- B. The third element of the second column of arr2d.
- C. The second element of the third row of arr2d.
- D. The second element of the third column of arr2d.

### Q7: What is the result of the following code `arr2d[1][2] = 12`?

- A. It changes the third element of the second row of arr2d to 12.
- B. It changes the third element of the second column of arr2d to 12.
- C. It changes the second element of the third row of arr2d to 12.
- D. It changes the second element of the third column of arr2d to 12.

### Q8: How do you compute the union of two arrays arr1 and arr2?

- A. np.union1d(arr1, arr2)
- B. np.union(arr1, arr2)
- C. np.union2d(arr1, arr2)
- D. np.union3d(arr1, arr2)

### Q9: How do you compute the dot product of two arrays arr1 and arr2?

- A. np.dot(arr1, arr2)
- B. np.cross(arr1, arr2)
- C. np.multiply(arr1, arr2)
- D. np.divide(arr1, arr2)

### Q10: How do you compute the inverse of a matrix mat?

- A. linalg.norm(mat)
- B. linalg.inv(mat)
- C. linalg.reverse(mat)
- D. linalg.flip(mat)
