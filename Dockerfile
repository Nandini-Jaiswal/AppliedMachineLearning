# Use Python 3.9 slim base image - a lightweight version of Python official image
FROM python:3.9-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the contents of local Assignment_4 directory to the container's working directory
COPY ./Assignment_4 .

# Copy the requirements.txt file to the container's working directory
COPY requirements.txt .

# Install Python dependencies from requirements.txt
# --no-cache-dir reduces the image size by not caching pip packages
RUN pip install --no-cache-dir -r requirements.txt

# Inform Docker that the container will listen on port 5000
EXPOSE 5000

# Command to run when the container starts
# Executes "python app.py" to start the application
CMD ["python", "app.py"]