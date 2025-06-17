#!/bin/sh
set -ex
echo "Script started"
# -e: Exit immediately if a command exits with a non-zero status
# -x: Print each command before executing it

host="selenium"
# The Docker Compose service name of the Selenium container
port=4444
# The port Selenium listens on inside the container

echo "Waiting for Selenium at $host:$port..."

# Loop until Selenium is accessible on the specified host and port
while ! nc -z $host $port; do
  echo "Selenium not ready yet..."
  sleep 1
done

echo "Selenium is up - starting tests..."

exec pytest tests/web_tests/admin_page/test_create_room.py
# Replace the shell with the pytest process
