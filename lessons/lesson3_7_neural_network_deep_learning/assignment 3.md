# Assignment

## Instructions

### Task: Building a Neural Network for Wine Classification

In this assignment, you will build and train a neural network using PyTorch to classify wine varieties based on their chemical attributes. You will use the Wine dataset, a classic machine learning dataset that contains the results of chemical analyses of wines grown in the same region in Italy but derived from three different cultivars.

#### Dataset

The Wine dataset consists of 13 features:

1. Alcohol
2. Malic acid
3. Ash
4. Alcalinity of ash
5. Magnesium
6. Total phenols
7. Flavanoids
8. Nonflavanoid phenols
9. Proanthocyanins
10. Color intensity
11. Hue
12. OD280/OD315 of diluted wines
13. Proline

The target variable is the class of wine (1, 2, or 3).

#### Requirements

1. Load the Wine dataset from scikit-learn
2. Preprocess the data (standardize features)
3. Split the data into training and testing sets
4. Build a multi-layer neural network using PyTorch with:
   - An input layer (matching the number of features)
   - At least one hidden layer with ReLU activation
   - An output layer with appropriate activation for classification
5. Train your model using an appropriate loss function and optimizer
6. Evaluate your model's performance on the test set
7. Experiment with different network architectures or hyperparameters to improve performance

#### Starter Code

```python
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

# Load the Wine dataset
wine = load_wine()
X, y = wine.data, wine.target

# Preprocess the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Convert to PyTorch tensors
X_train_tensor = torch.FloatTensor(X_train)
X_test_tensor = torch.FloatTensor(X_test)
y_train_tensor = torch.LongTensor(y_train)
y_test_tensor = torch.LongTensor(y_test)

# TODO: Define your neural network

# TODO: Initialize the network

# TODO: Create model, define loss function and optimizer

# TODO: Implement training loop

# TODO: Evaluate the model on test data
```

## Submission

- Submit the URL of the GitHub Repository that contains your work to NTU black board.
- Should you reference the work of your classmate(s) or online resources, give them credit by adding either the name of your classmate or URL.
