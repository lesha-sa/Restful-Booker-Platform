#!/bin/bash
# before_launching_docker.sh — preparing the project after the clone

# Go to the project root (where Dockerfile and wait-for-selenium.sh are located)
cd "$(dirname "$0")" || exit 1

# Make the wait-for-selenium.sh script executable
chmod +x wait-for-selenium.sh

# Convert string endings to Unix format (if copied from Windows)
if command -v dos2unix >/dev/null 2>&1; then
    dos2unix wait-for-selenium.sh
else
    echo "dos2unix not found, skip conversion."
fi

echo "The project is ready for a Docker build."
