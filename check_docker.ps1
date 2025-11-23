# Запускаем docker info и смотрим на ExitCode
docker info > $null 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "Docker is running."
} else {
    Write-Host "Docker is NOT running."
}
