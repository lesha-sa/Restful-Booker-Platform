Write-Host "Starting tests..."

# Clearing old Allure results
if (Test-Path -Path "./allure-results") {
    Write-Host "Cleaning old Allure results..."
    Remove-Item -Path "./allure-results/*" -Recurse -Force
}

# Running tests with Allure report generation
pytest --alluredir=./allure-results
