# Use the official Python image as a base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /code

# Copy the requirements.txt file into the working directory
COPY requirements.txt /code

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the working directory
COPY . /code

# Specify the command to run application
CMD ["python", "app.py"]

