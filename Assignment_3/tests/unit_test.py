from score import score
import pickle

with open('assignment_3/best_model.pkl', 'rb') as file:
    model = pickle.load(file)

def test_score():
    """Test the score function with various inputs"""
    text = "This is a test message"
    prediction, propensity = score(text, model, 0.5)
    assert isinstance(prediction, int), "Prediction should be an integer"
    assert isinstance(propensity, float), "Propensity should be a float"
    assert 0 <= propensity <= 1, "Propensity should be between 0 and 1"
    assert prediction in [0, 1], "Prediction should be either 0 or 1"
    

# Test cases
def test_score_smoke():
    """Smoke test to check if function runs without crashing"""
    text = "This is a test message"
    prediction, propensity = score(text, model, 0.5)
    # Check if the function runs without any exceptions
    assert True  # If we get here, the function didn't crash

def test_score_format():
    """Test if input/output formats/types are as expected"""
    text = "Another test message"
    prediction, propensity = score(text, model, 0.5)
    
    assert isinstance(text, str), "Input text should be a string"
    assert isinstance(prediction, int), "Prediction should be an integer"
    assert isinstance(propensity, float), "Propensity should be a float"

def test_prediction_values():
    """Test if prediction is either 0 or 1"""
    texts = [
        "Free money now!!!",
        "Hello, how are you doing today?",
        "This is a neutral message"
    ]
    
    for text in texts:
        prediction, _ = score(text, model, 0.5)
        assert prediction in [0, 1], f"Prediction should be 0 or 1, got {prediction}"

def test_propensity_range():
    """Test if propensity score is between 0 and 1"""
    texts = [
        "Win a free iPhone! Click now!",
        "Meeting tomorrow at 10am",
        "Nigerian prince needs your help"
    ]
    
    for text in texts:
        _, propensity = score(text, model, 0.5)
        assert 0 <= propensity <= 1, f"Propensity should be between 0 and 1, got {propensity}"

def test_threshold_zero():
    """Test if threshold=0 makes prediction always 1"""
    texts = [
        "This should be ham",
        "Normal message",
        "Regular email content"
    ]
    
    for text in texts:
        prediction, _ = score(text, model, 0.0)
        assert prediction == 1, f"With threshold=0, prediction should be 1, got {prediction}"

def test_threshold_one():
    """Test if threshold=1 makes prediction always 0"""
    texts = [
        "FREE MONEY!!!",
        "Urgent! Click this link!",
        "You've won a prize"
    ]
    
    for text in texts:
        prediction, _ = score(text, model, 1.0)
        assert prediction == 0, f"With threshold=1, prediction should be 0, got {prediction}"

def test_obvious_spam():
    """Test on obvious spam text"""
    spam_texts = [
        "FREE FREE FREE get your free gift now!!!",
        "You've won $1,000,000! Click here to claim!",
        "Urgent: Your account has been compromised. Send password to reset."
    ]
    
    for text in spam_texts:
        prediction, propensity = score(text, model, 0.5)
        assert prediction == 1, f"Obvious spam should be predicted as 1, got {prediction}"

def test_obvious_ham():
    """Test on obvious non-spam text"""
    ham_texts = [
        "Hello, how are you doing today?",
        "The meeting is scheduled for tomorrow at 3pm.",
        "Please find attached the report we discussed yesterday."
    ]
    
    for text in ham_texts:
        prediction, propensity = score(text, model, 0.5)
        assert prediction == 0, f"Obvious ham should be predicted as 0, got {prediction}"