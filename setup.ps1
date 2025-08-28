# setup.ps1 — prepares the project and runs tests (Windows)
set-StrictMode -Version Latest

# Go to the script directory (project root)
cd "$(Split-Path -Parent $MyInvocation.MyCommand.Definition)"

# 1️⃣ Create venv if it doesn't exist
if (-not (Test-Path "./venv")) {
    py -3.11 -m venv venv
    Write-Host 'Virtual environment created.'
} else {
    Write-Host 'Virtual environment already exists.'
}

# 2️⃣ Activate venv
& .\venv\Scripts\Activate.ps1

# 3️⃣ Update pip and install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
