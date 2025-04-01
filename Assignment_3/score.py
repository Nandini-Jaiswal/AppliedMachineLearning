import string
import nltk
from nltk.corpus import stopwords
import warnings
import sklearn
import sklearn.pipeline
nltk.download('stopwords')
warnings.filterwarnings('ignore')

def preprocess_text(text):
    """
    Preprocesses text by converting to lowercase, removing punctuation and stopwords.

    Args:
        text (str): Input text to preprocess

    Returns:
        str: Cleaned text in lowercase with punctuation and stopwords removed
    """
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    stop_words = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

def score(text: str, model: sklearn.pipeline.Pipeline, threshold: float) -> tuple[bool, float]:
    """Score a single text input using a trained model and threshold.

    This function processes a text input and returns both the binary prediction
    and the probability score for spam content classification.

    Args:
        text (str): The input text to be classified
        model (sklearn.pipeline.Pipeline): Trained sklearn Pipeline model for classification
        threshold (float): Classification threshold for converting probability to binary prediction

    Returns:
        tuple: A tuple containing:
            - prediction (int): Binary prediction (1 for spam, 0 for ham)
            - propensity (float): Probability score for spam class
    """
    text_list = [preprocess_text(text)]
    propensity = model.predict_proba(text_list)[:, 1][0]
    prediction = True if propensity >= threshold else False
    return prediction, propensity
