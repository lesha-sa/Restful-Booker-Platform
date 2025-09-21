Write-Host "Running tests on Chrome..."

# Clearing old Allure results
if (Test-Path -Path "./allure-results/chrome") {
    Write-Host "Cleaning old Allure results..."
    Remove-Item -Path "./allure-results/*" -Recurse -Force
}

# Running tests on Chrome
pytest --alluredir=./allure-results/chrome --browser=chrome

Write-Host "Tests finished. Allure results in ./allure-results"

# Opening a report
allure serve ./allure-results/chrome