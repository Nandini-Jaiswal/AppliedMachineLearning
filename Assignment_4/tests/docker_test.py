import time
import requests
import subprocess
import os

def test_docker():
    """Test if the docker container is running"""

    print("Building Docker image...")
    build_command = "docker build -t docker-flask-app ."
    result = os.system(build_command)
    if result != 0:
        raise Exception(f"Docker build failed with exit code {result}")
    print("Docker image built successfully.")
    
    print("Starting Docker container...")
    run_command = "docker run -d -p 5000:5000 --name docker-flask-container docker-flask-app"
    result = os.system(run_command)
    if result != 0:
        raise Exception(f"Docker run failed with exit code {result}")
    
    time.sleep(20)

    response = requests.get("http://127.0.0.1:5000/test")

    assert response.status_code == 200
    assert response.json() == {"message": 'Welcome to the scoring API!'}

def test_home_okay():
    """Test on get method"""
    response = requests.get("http://127.0.0.1:5000/test")
    assert response.status_code == 200

def test_home_post():
    """Test on post method with JSON input"""
    response = requests.post("http://127.0.0.1:5000/score", json={"text": "hello"})
    assert response.status_code == 200

def test_obvious_spam():
    """Test on obvious spam text"""
    spam_texts = [
        "FREE FREE FREE get your free gift now!!!",
        "You've won $1,000,000! Click here to claim!",
        "Urgent: Your account has been compromised. Send password to reset."
    ]
    
    for text in spam_texts:
        response = requests.post("http://127.0.0.1:5000/score", json={"text": text})
        prediction = response.json()["prediction"]
        assert prediction == 'spam', f"Obvious spam should be predicted as 1, got {prediction}"

def test_obvious_ham():
    """Test on obvious non-spam text"""
    ham_texts = [
        "Hello, how are you doing today?",
        "The meeting is scheduled for tomorrow at 3pm.",
        "Please find attached the report we discussed yesterday."
    ]
    
    for text in ham_texts:
        response = requests.post("http://127.0.0.1:5000/score", json={"text": text})
        prediction = response.json()["prediction"]
        assert prediction == 'ham', f"Obvious ham should be predicted as 0, got {prediction}"


    print("Stopping Docker container...")
    os.system("docker stop docker-flask-container") 
    
    print("Removing Docker container...")
    os.system("docker rm docker-flask-container")    
    
    print("Docker container cleaned up.")