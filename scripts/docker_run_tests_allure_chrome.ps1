# Abort execution on error
$ErrorActionPreference = "Stop"

Write-Host "Running tests on Chrome..."

# Clearing out the old Allure results
if (Test-Path -Path "./allure-results/chrome") {
    Write-Host "Cleaning old Allure results..."
    Remove-Item -Path "./allure-results/chrome/*" -Recurse -Force
}

# Running tests in Chrome
docker-compose run --rm tests pytest --browser=chrome --alluredir=./allure-results/chrome

Write-Host "Tests finished. Allure results in ./allure-results/chrome"

# Opening a report via Allure
allure serve ./allure-results/chrome

