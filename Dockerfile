# Use the official Python 3.9 slim base image
FROM python:3.9-slim
# Set the working directory inside the container to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app
# Install Python dependencies from requirements.txt with --no-cache-dir option
RUN pip install --no-cache-dir -r requirements.txt
# Install the Gunicorn web server
RUN pip install gunicorn
# Expose port 5000 to allow external connections
EXPOSE 5000

# Specify the command to run when the container starts
ENTRYPOINT ["gunicorn", "flsk:app", "-b", "0.0.0.0:5000"]
