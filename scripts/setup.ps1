# setup.ps1 — prepares dependencies for the project
set-StrictMode -Version Latest

#  Navigate to project root regardless of where script is executed
cd "$PSScriptRoot\.."

# Activate existing venv
& .\.venv\Scripts\Activate.ps1

# Update pip
python -m pip install --upgrade pip

# Install/update dependencies
python -m pip install -r "./requirements.txt"

Write-Host "Dependencies are up-to-date!"