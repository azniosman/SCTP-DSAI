# Assignment

## Instructions

Use the following code as a starting point to load the rotten tomatoes dataset:

```python
from datasets import load_dataset

# Load the Rotten Tomatoes dataset
dataset = load_dataset("rotten_tomatoes")

# Print the dataset information
print(dataset)

# Example: Accessing the training split
train_dataset = dataset["train"]

# Print the first example in the training set
print(train_dataset[0])
```

**Model Application:**

- Load a pre-trained sentiment analysis model from Hugging Face Transformers.
- Apply the model to a subset of the chosen dataset (e.g., the first 1000 samples from the training set).
- Evaluate the model's performance. You can start with qualitative analysis (inspecting predictions) and then explore quantitative metrics.

## Submission

- Submit the URL of the GitHub Repository that contains your work to NTU black board.
- Should you reference the work of your classmate(s) or online resources, give them credit by adding either the name of your classmate or URL.
