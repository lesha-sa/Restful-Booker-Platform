FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /python-app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Install netcat (nc) to check Selenium availability
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*
COPY wait-for-selenium.sh /wait-for-selenium.sh
# Make the Selenium wait script executable
RUN chmod +x /wait-for-selenium.sh
# Set default command to wait for Selenium and then run tests
CMD ["/wait-for-selenium.sh"]



