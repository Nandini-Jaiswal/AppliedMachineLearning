import requests
import subprocess

def test_docker():
    """Test if the docker container is running"""

    print("Building the Docker image...")
    subprocess.run(
        ["docker", "build", "-t", "docker-flask-app", "."],
        check=True,
        capture_output=True,
        text=True,
    )
    print("Docker image built successfully.")\
    
    print("Starting the Docker container...")
    subprocess.run(["docker", "run", "-d", "-p", "5000:5000", "--name", "docker-flask-container", "docker-flask-app"], check=True, capture_output=True, text=True)


    response = requests.get("http://127.0.0.1:5000/test")
    assert response.status_code == 200
    assert response.json() == {"message": "Flask app is running successfully."}
