## Workflow Explanation

### [prepare.ipynb](./prepare.ipynb)

1. **Setting up DVC**: Initializes Data Version Control (DVC) for tracking datasets.

2. **Data Reading and Processing**: 
    - Reads SMS data from 'SMSSpamCollection'
    - Creates utility functions for data handling
    - Processes 5572 messages

3. **Data Splitting**:
    - Splits data into train (70%), validation (10%), and test (20%) sets
    - Saves splits as CSV files

4. **DVC Configuration**:
    - Sets up Google Drive as remote storage
    - Tracks CSV files with DVC
    - Creates version control for datasets

### [train.ipynb](./train.ipynb)

1. **MLflow Integration**:
    - Sets up experiment tracking
    - Configures model registry
    - Logs parameters, metrics, and models

2. **Model Training**:
    - Implements 5 classifiers:
      - Random Forest
      - Decision Tree
      - Logistic Regression
      - Support Vector Classifier
      - Multinomial Naive Bayes
    - Uses GridSearchCV for hyperparameter tuning
    - Evaluates using AUC-PR scores

3. **Results**:
    | Model | AUC-PR Score |
    |-------|--------------|
    | MultinomialNB | 0.9369 |
    | LogisticRegression | 0.9226 |
    | SVC | 0.9173 |
    | RandomForest | 0.9008 |
    | DecisionTree | 0.8312 |

4. **Best Model**: MultinomialNB achieved highest performance with 0.9369 AUC-PR score.