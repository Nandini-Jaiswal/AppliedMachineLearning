import os
import time
import requests
import subprocess

def test_flask():
    """Test if Flask app is running"""
    process = subprocess.Popen("python Assignment_3/app.py", shell=True)
    time.sleep(5)
    try:
        response = requests.get("http://127.0.0.1:5000/test")
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        assert response.json() == {"message": "Welcome to the scoring API!"}, f"Unexpected response: {response.json()}"
        print("Flask app is running successfully.")
    finally:
        process.terminate()
        process.wait()
        print("Flask app has been shut down.")

def test_home_okay(client):
    """Test on get method"""
    response = client.get("/test")
    assert response.status_code == 200

def test_home_post(client):
    """Test on post method with JSON input"""
    response = client.post("/score", json={"text": "hello"})
    assert response.status_code == 200

def test_obvious_spam(client):
    """Test on obvious spam text"""
    spam_texts = [
        "FREE FREE FREE get your free gift now!!!",
        "You've won $1,000,000! Click here to claim!",
        "Urgent: Your account has been compromised. Send password to reset."
    ]
    
    for text in spam_texts:
        response = client.post("/score", json={"text": text})
        prediction = response.json["prediction"]
        assert prediction == 'spam', f"Obvious spam should be predicted as 1, got {prediction}"

def test_obvious_ham(client):
    """Test on obvious non-spam text"""
    ham_texts = [
        "Hello, how are you doing today?",
        "The meeting is scheduled for tomorrow at 3pm.",
        "Please find attached the report we discussed yesterday."
    ]
    
    for text in ham_texts:
        response = client.post("/score", json={"text": text})
        prediction = response.json["prediction"]
        assert prediction == 'ham', f"Obvious ham should be predicted as 0, got {prediction}"