# setup.ps1 — prepares the project and runs tests (Windows)
set-StrictMode -Version Latest

# Navigate to project root regardless of where script is executed
cd "$PSScriptRoot\.."

# Create venv if it doesn't exist
if (-not (Test-Path "./venv")) {
    py -3.11 -m venv venv
    Write-Host 'Virtual environment created.'
} else {
    Write-Host 'Virtual environment already exists.'
}

# Activate venv
& .\venv\Scripts\Activate.ps1

# Update pip and install dependencies
python -m pip install --upgrade pip
python -m pip install -r "./requirements.txt"
