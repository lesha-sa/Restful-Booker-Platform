Write-Host "Running tests on Chrome..."

# Clearing old Allure results
if (Test-Path -Path "./allure-results/firefox") {
    Write-Host "Cleaning old Allure results..."
    Remove-Item -Path "./allure-results/*" -Recurse -Force
}

# Running tests on Firefox
pytest --alluredir=./allure-results/firefox --browser=firefox

Write-Host "Tests finished. Allure results in ./allure-results"

# Opening a report
allure serve ./allure-results/firefox