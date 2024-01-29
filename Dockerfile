# Slim version of Python
FROM python:3.8.12-slim

# Download Package Information
RUN apt-get update -y

# Install Tkinter
RUN apt-get install tk -y

# Set the working directory
WORKDIR /app/

# Copy the local files to the container
COPY . /app/

# Commands to run Tkinter application
CMD ["python", "/app/main.py"]