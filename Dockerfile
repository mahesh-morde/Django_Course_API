# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the Docker container
COPY . .

# Expose the port that the app runs on
EXPOSE 8000

# Run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
