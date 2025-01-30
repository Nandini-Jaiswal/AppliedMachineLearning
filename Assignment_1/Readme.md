## Workflow Explanation

### [prepare.ipynb](./prepare.ipynb)

1. **Import Necessary Modules**: The notebook starts by importing essential libraries such as `nltk`, `pandas`, `matplotlib`, `seaborn`, and `sklearn`.

2. **Reading the File**: The SMS Spam Collection dataset is read into a pandas DataFrame.

3. **Preprocessing the Text**: The text messages are preprocessed by converting to lowercase, removing punctuation, and removing stopwords.

4. **Exploratory Data Analysis (EDA)**: The dataset is analyzed to understand the distribution of labels and message lengths. Visualizations such as count plots and histograms are created.

5. **Wordclouds**: Word clouds are generated to visualize the most common words in ham and spam messages.

6. **Splitting the Dataset**: The dataset is split into training, validation, and test sets. These splits are saved to CSV files for further processing.

### [train.ipynb](./train.ipynb)

1. **Importing Necessary Libraries**: Libraries for data manipulation, model training, and evaluation are imported.

2. **Loading and Cleaning Data**: The training, validation, and test datasets are loaded and cleaned.

3. **Combining Training and Validation Data**: The training and validation datasets are combined for hyperparameter tuning using `GridSearchCV`.

4. **Training Various Classifiers**: Different classifiers such as Random Forest, Decision Tree, Logistic Regression, SVC, and Multinomial Naive Bayes are trained using pipelines. Hyperparameters are tuned using `GridSearchCV`.

5. **Evaluating Classifiers**: Each classifier is evaluated on the test set. Classification reports and confusion matrices are generated to assess performance.

6. **Model Performance Comparison**: The performance of all classifiers is compared based on accuracy, precision, recall, and F1-score.

## Results Discussion

- **Random Forest**: Achieved high accuracy and F1-score, indicating good performance in both ham and spam detection.
- **Decision Tree**: Performed well but slightly less accurate than Random Forest.
- **Logistic Regression**: Showed excellent performance with high precision and recall for both classes.
- **SVC**: Similar performance to Logistic Regression, with high accuracy and F1-score.
- **Multinomial Naive Bayes**: Also performed well, particularly in detecting spam messages.

Overall, Logistic Regression and SVC provided the best results, with Random Forest being a close contender. The best performance was by `Support Vector Classifier`.