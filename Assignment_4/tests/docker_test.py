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
    
    time.sleep(10)

    response = requests.get("http://127.0.0.1:5000/test")

    assert response.status_code == 200
    assert response.json() == {"message": "Flask app is running successfully"}