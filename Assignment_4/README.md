# Assignment 4: Containerization and Continuous Integration for Spam Classification

This repository involve containerizing the Flask app using Docker, testing it, and integrating it with a basic continuous integration (CI) setup using Git pre-commit hooks.

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

The tests folder currently contains the most important file:

- [`docker_test.py`](./tests/docker_test.py) - This script performs automated tests for the Flask scoring API running inside a Docker container. It verifies that the container runs correctly and that the API responds as expected to various inputs.

#### Key Functions:

1. **`test_docker()`**  
   - Builds the Docker image using the `Dockerfile`.
   - Runs the container and waits for the server to start.
   - Sends a GET request to the `/test` endpoint to ensure the server is running.
   - Asserts that the server responds with the expected welcome message.

2. **`test_home_okay()`**  
   - Checks if the `/test` endpoint responds successfully (HTTP 200).

3. **`test_home_post()`**  
   - Sends a POST request to `/score` with a sample input (`"hello"`).
   - Ensures the endpoint returns a successful response.

4. **`test_obvious_spam()`**  
   - Tests the API with clearly spammy inputs.
   - Asserts that the model classifies them as `'spam'`.

5. **`test_obvious_ham()`**  
   - Tests with clearly non-spam (ham) inputs.
   - Asserts that the model classifies them as `'ham'`.

6. **Docker Cleanup**  
   - At the end of the tests, the Docker container is stopped and removed to clean up resources.

### 4. `Dockerfile`

The `Dockerfile` defines the instructions to build a lightweight Docker image for the Flask scoring app.

1. **Base Image**  
   Uses the lightweight `python:3.9-slim` image to minimize image size.

2. **Working Directory**  
   Sets the working directory inside the container to `/app`.

3. **Copy Files**  
   - Copies all application files from the local `Assignment_4` directory into the container.
   - Copies `requirements.txt` for dependency installation.

4. **Install Dependencies**  
   Installs Python packages listed in `requirements.txt` using `pip` with `--no-cache-dir` to reduce image size.

5. **Expose Port**  
   Exposes port `5000` so the Flask app can be accessed externally.

6. **Run the App**  
   Sets the default command to run `app.py` when the container starts:
   `python app.py`

### 5. Pre-commit Hook (`pre-commit`)

The **pre-commit Git hook script** ensures that all tests pass before allowing a commit to the repository.

1. **Locates the Git Repo Root**  
   Finds the top-level directory of your Git repository using `git rev-parse`.

2. **Checks for a Virtual Environment**  
   Verifies that a `venv/` directory exists. If found, it activates the environment:
   - Supports both Windows (`Scripts/activate`) and Unix (`bin/activate`).

3. **Runs Tests with `pytest`**  
   Executes all tests inside the `Assignment_4` directory.

4. **Handles Test Results**  
   - If **tests pass**, the commit proceeds.
   - If **tests fail**, the commit is aborted with an error message.

5. **Deactivates the Virtual Environment**  
   After tests complete (pass or fail), it safely deactivates the environment.

## Comments

You need to run `git config core.hooksPath .githooks` to set the hooks path.