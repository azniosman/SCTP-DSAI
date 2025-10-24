# Assignment

## Instructions

Complete the following exercise using Python.

Loan Approval Prediction:

Using the Loan Approval dataset, create an end-to-end workflow for predicting loan approval. Your workflow should include:

- Data loading and exploration
- Data preprocessing (handling missing values, encoding categorical variables, feature scaling)
- Feature selection
- Model training (using logistic regression and KNN)
- Model evaluation (using accuracy, precision, recall, F1-score and ROC AUC score)

```python
import pandas as pd
import numpy as np

# Load the dataset
loan_data = pd.read_csv('https://raw.githubusercontent.com/prasertcbs/basic-dataset/refs/heads/master/Loan-Approval-Prediction.csv')

# Split features and target
X = loan_data.drop('Loan_Status', axis=1)
y = loan_data['Loan_Status']
```

## Submission

- Submit the URL of the GitHub Repository that contains your work to NTU black board.
- Should you reference the work of your classmate(s) or online resources, give them credit by adding either the name of your classmate or URL.
