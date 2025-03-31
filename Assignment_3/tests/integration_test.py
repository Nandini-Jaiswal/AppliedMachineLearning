import os
import time
import requests
import subprocess

def test_flask():
    # Start Flask app in a separate process
    process = subprocess.Popen("python Assignment_3/app.py", shell=True)

    # Give Flask time to start
    time.sleep(5)

    try:
        # Test the response from the localhost endpoint
        response = requests.get("http://127.0.0.1:5000/test")
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        print("Flask app is running successfully.")
    finally:
        # Kill the Flask process
        process.terminate()
        process.wait()  # Wait for the process to finish
        print("Flask app has been shut down.")

def test_home_okay(client):
    """test get method"""
    response = client.get("/test")
    assert response.status_code == 200

def test_home_post(client):
    """test post method with JSON input"""
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
        assert prediction == 1, f"Obvious spam should be predicted as 1, got {prediction}"

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
        assert prediction == 0, f"Obvious ham should be predicted as 0, got {prediction}"