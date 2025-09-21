# Test Automation Framework for UI Web Testing  
https://automationintesting.online/

---

## Table of Contents
1. [Preparation before Running Tests](#preparation-before-running-tests)  
2. [Test Framework Configuration and Setup](#test-framework-configuration-and-setup)  
3. [Running Tests Locally](#running-tests-locally)  
4. [Running Tests with Docker Compose](#running-tests-with-docker-compose)  
5. [CI/CD Integration with GitHub Actions](#cicd-integration-with-github-actions)  
6. [Additional Notes](#additional-notes)  

---

## Preparation before Running Tests

Install Python 3.11 (if not): https://www.python.org/downloads/release/python-3119/

Run the preparation script.
The script creates a virtual environment, puts all dependencies and runs the tests.
```bash
./setup.ps1
```

## Running Tests Locally
1. Run tests in Chrome without allure reports:
```bash
pytest tests/ --browser=chrome
```
Run tests in Firefox without allure reports:
```bash
pytest tests/ --browser=firefox
```
2. Running tests in Chrome with Allure report generation and deleting old reports and running new reports:
```bash
 ./scripts/local_run_tests_allure_chrome.ps1
```
Running tests in Firefox with Allure report generation and deleting old reports and running new reports:
```bash
 ./scripts/local_run_tests_allure_firefox.ps1
```
3. To view Allure reports Chrome
```bash
allure serve ./allure-results/chrome
```
To view Allure reports Firefox
```bash
allure serve ./allure-results/firefox
```
4. All test logs are saved in the ./logs folder.
To view it, just open the required file in any text editor.

## Running Tests with Docker Compose
Overview
Tests run inside a Docker container. The container waits for the Selenium standalone Chrome or Firefox container
to be ready before executing tests

Files involved
1. Dockerfile — builds Python test environment, installs dependencies, copies project, sets wait script as entrypoint
2. Docker-compose.yml — defines services:
2.1 Selenium-chrome and selenium-firefox — standalone Selenium servers on ports 4444 and 4445.
2.2 Tests — test runner container built from Dockerfile, depends on Selenium and database, mounts project
3. and logs directories, runs wait script and executes tests.
3.  wait-for-selenium.sh — bash script that waits until Selenium server is available on selenium:4444.

How to run
1. Prepare the environment (make wait-for-selenium.sh executable and convert it to Unix-format):
```bash
./scripts/before_launching_docker.ps1
```
2. Ensure Docker and Docker Compose are installed and running.
3. Building Docker images. Reassembles all images anew, 
ignoring the cache, so that tests run with the actual changes.
```bash
docker compose build --no-cache
```
4. Running tests in Chrome and automatically terminating containers.
Containers will automatically stop after the tests are completed.
All logs and test results are saved to the specified volumes (./logs, ./allure-results/chrome).
```bash
./scripts/docker_run_tests_allure_chrome.ps1
```
Running tests in Firefox and automatically terminating containers.
Containers will automatically stop after the tests are completed.
All logs and test results are saved to the specified volumes (./logs, ./allure-results/firefox).
```bash
./scripts/docker_run_tests_allure_firefox.ps1
```
5. Test logs from the container are saved in the ./logs folder on the local machine.
You can open them there just as you would when running locally.
6. Full clear docker
```bash
docker system prune -a --volumes
```
## CI/CD Integration with GitHub Actions
This project uses GitHub Actions for continuous integration.

Workflow summary:
1. Runs on pushes or pull requests to branch features/A.
2. Checks out the repository.
3. Builds and runs Docker Compose to start Selenium and run tests.
4. Uploads logs as artifacts for review.
5. Outputs success or failure message to console.

## Additional Notes
1. Environment variables for test container are set in docker-compose.yml:

  SELENIUM_CHROME_URL=http://selenium-chrome:4444/wd/hub   # Chrome Selenium server inside Docker network
  SELENIUM_FIREFOX_URL=http://selenium-firefox:4444/wd/hub  # Firefox Selenium server inside Docker network
  LOG_PATH=/app/logs                                        # Directory for storing logs
  ALLURE_RESULTS=/app/allure-results                        # Directory for storing Allure results
  
2. wait-for-selenium.sh ensures tests don’t start before Selenium server is ready.
3. Logs are mounted as a volume to ./logs on host, so you can access test logs outside the container.
4. Keep your local repository updated with remote branches (git pull) to avoid conflicts.