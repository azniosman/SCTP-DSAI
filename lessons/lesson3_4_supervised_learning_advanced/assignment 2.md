# Assignment

## Instructions

1.  **Regularization**:

    - Use the `diabetes` dataset from `sklearn.datasets`.
    - Compare the performance (Mean Squared Error) of `LinearRegression`, `Ridge`, and `Lasso` models.
    - Tune the `alpha` parameter for `Ridge` and `Lasso` using `GridSearchCV` with cross-validation to find the optimal regularization strength.

    ```python
    from sklearn.datasets import load_diabetes

    # Load the diabetes dataset
    diabetes = load_diabetes()
    ```

2.  **Ensemble Methods**:

    - Use the `breast_cancer` dataset from `sklearn.datasets`.
    - Compare the performance (F1 Score and AUC) of `DecisionTreeClassifier`, `RandomForestClassifier`, and `GradientBoostingClassifier`.
    - Tune the hyperparameters of each classifier using `GridSearchCV` with cross-validation.

    ```python
    from sklearn.datasets import load_breast_cancer

    # Load the breast cancer dataset
    breast_cancer = load_breast_cancer()
    ```

## Submission

- Submit the URL of the GitHub Repository that contains your work to NTU black board.
- Should you reference the work of your classmate(s) or online resources, give them credit by adding either the name of your classmate or URL.
