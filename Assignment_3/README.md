<!-- @format -->

# Assignment 3: Flask Server for Spam Classification

This repository contains a simple flask server that serves an implementation of a spam classification system using machine learning.

## Files and Directories

### 1. [`score.py`](./score.py)

This file contains the core functionality for preprocessing text and scoring it using a trained machine learning model.

#### Key Functions:

- **`preprocess_text(text)`**:

  - Preprocesses text by converting to lowercase, removing punctuation and stopwords.
  - Returns cleaned text.

- **`score(text, model, threshold, vectorizer)`**:
  - Score a single text input using a trained model and threshold.
  - Returns a tuple containing the prediction (True for spam, False for ham) and the propensity score.

### 2. [`app.py`](./app.py)

The `app.py` contains a flask server that implements the spam/ham classification system.
It has two endpoints:

- `/test` - endpoint for checking if the API is running.
- `/score` - endpoint for scoring text

### 3. `tests/`

The tests folder currently contains 3 important files:

- [`conftest.py`](./tests/conftest.py) - contains the configuration for the integration tests.
- [`integration_test.py`](./tests/integration_test.py) - contains integration tests which includes running the flask server and closing it.
- [`unit_test.py`](./tests/unit_test.py) - contains unit tests that test the score api.

## Comments

I have also added the [`pytest`](https://github.com/Nandini-Jaiswal/AppliedMachineLearning/actions) and [`codecov`](https://app.codecov.io/gh/Nandini-Jaiswal/AppliedMachineLearning?search=&displayType=list) (to view code coverage reports) to the github workflows.