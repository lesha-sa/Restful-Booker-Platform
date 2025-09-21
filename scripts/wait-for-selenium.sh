#!/bin/sh
# Enable modes:
# -e: abort immediately if any command terminates with an error
# -x: output each command before executing it
set -ex

echo "Script started"

# Define Selenium host (service name in Docker Compose)
host="selenium"

# Port on which Selenium listens for WebDriver connections
port=4444

echo "Waiting for Selenium at $host:$port..."

# Waiting cycle: check Selenium availability on the specified host and port
while ! nc -z $host $port; do
  # If not yet available, display a message
  echo "Selenium not ready yet..."
  # Wait 1 second for the next attempt
  sleep 1
done

echo "Selenium is up - starting tests..."
# execute pytest for the tests folder
# exec replaces the current process with pytest (does not create an additional shell process)
exec pytest tests
