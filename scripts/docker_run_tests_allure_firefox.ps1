# Abort execution on error
$ErrorActionPreference = "Stop"

Write-Host "Running tests on Firefox..."

# Clearing out the old Allure results
if (Test-Path -Path "./allure-results/firefox") {
    Write-Host "Cleaning old Allure results..."
    Remove-Item -Path "./allure-results/firefox/*" -Recurse -Force
}

# Running tests in Firefox
docker-compose run --rm tests pytest --browser=firefox --alluredir=./allure-results/firefox

Write-Host "Tests finished. Allure results in ./allure-results/firefox"

# Opening a report via Allure
allure serve ./allure-results/firefox
