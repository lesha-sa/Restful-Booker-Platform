Write-Host "Preparing project for Docker..."

# Define the path to the wait-for-selenium.sh script relative to the current script
$waitScript = Join-Path $PSScriptRoot "wait-for-selenium.sh"

# Check if the script exists
if (Test-Path $waitScript) {
    Write-Host "Making wait-for-selenium.sh executable..."

    # Make the file executable via git (important for Linux/Mac and Docker)
    git update-index --chmod=+x $waitScript

    # Check if the dos2unix command is available
    if (Get-Command dos2unix -ErrorAction SilentlyContinue) {
        # Please be advised that conversion to Unix format (LF) will be performed
        Write-Host "Converting wait-for-selenium.sh to Unix format..."
        dos2unix $waitScript
    } else {
        Write-Host "dos2unix not found, skipping conversion."
    }
} else {
    Write-Warning "wait-for-selenium.sh not found at $waitScript"
}

Write-Host "Project prepared for Docker."
