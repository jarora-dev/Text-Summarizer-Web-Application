# Use the official Python image as the base image
FROM python:3.10.9
RUN apt-get update && \
    apt-get install -y build-essential python3-dev


# Set the working directory
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY /templates/ /app/templates/
COPY /app.py /app/app.py

# Expose the port the app will run on
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]
