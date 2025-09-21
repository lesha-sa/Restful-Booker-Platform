# Use the lightweight Python 3.11 image
FROM python:3.11-slim
# Disable stdout/stderr buffering so that logs are output at once
ENV PYTHONUNBUFFERED=1
# Set the working directory inside the container to /app
WORKDIR /app
# Copy the file with dependencies into the container
COPY requirements.txt .
# Install Python dependencies without cache to save space
RUN pip install --no-cache-dir -r requirements.txt
# Install netcat (nc) to check Selenium availability
# After installation, clear the apt cache to reduce the image size
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*
# Copy the scripts folder inside the container
COPY ./scripts /app/scripts
# Make the Selenium wait script executable
RUN chmod +x /app/scripts/wait-for-selenium.sh
# When the default container is started, this script will be executed,
# which waits for Selenium to be ready and runs pytest
CMD ["/app/scripts/wait-for-selenium.sh"]

