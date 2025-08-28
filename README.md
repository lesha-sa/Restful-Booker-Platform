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
.\setup.ps1
```

## Running Tests Locally
1. Run tests without allure reports:
```bash
pytest tests/
```
2. Running tests with Allure report generation and deleting old reports:
```bash
 .\run_tests_allure.ps1
```
3. To view Allure reports
```bash
allure serve ./allure-results
```
4. All test logs are saved in the ./logs folder.
To view it, just open the required file in any text editor.

## Running Tests with Docker Compose
Overview
Tests run inside a Docker container, which waits for a Selenium standalone Chrome container to be ready before starting.

Files involved
* Dockerfile — builds Python test environment, installs dependencies, copies project, sets wait script as entrypoint.

* docker-compose.yml — defines two services:

  * selenium: Selenium standalone Chrome server on port 4444

   * tests: test runner container built from Dockerfile, depends on selenium, mounts project and logs directories, runs wait script and tests.

* wait-for-selenium.sh — bash script that waits until Selenium server is available on selenium:4444.

How to run
1. Prepare the environment (make wait-for-selenium.sh executable and convert it to Unix-format):
```bash
./before_launching_docker.sh
```
2. Ensure Docker and Docker Compose are installed and running.
3. Building Docker images. Reassembles all images anew, 
ignoring the cache, so that tests run with the actual changes.
```bash
docker compose build --no-cache
```
4. Running tests and automatically terminating containers.
Containers will automatically stop after the tests are completed.
All logs and test results are saved to the specified volumes (./logs, ./allure-results).
```bash
docker compose up --abort-on-container-exit
```
5. After running tests, Allure results are saved in ./allure-results.
To open the report locally:
```bash
allure serve ./allure-results
```
6. Test logs from the container are saved in the ./logs folder on the local machine.
You can open them there just as you would when running locally.

## CI/CD Integration with GitHub Actions
This project uses GitHub Actions for continuous integration.

Workflow summary:
* Runs on pushes or pull requests to branch features/A.

* Checks out the repository.

* Builds and runs Docker Compose to start Selenium and run tests.

* Uploads logs as artifacts for review.

* Outputs success or failure message to console.

## Additional Notes
* Environment variables for test container are set in docker-compose.yml:

   * SELENIUM_URL=http://selenium:4444/wd/hub — Selenium server URL inside Docker network.
  
   * LOG_PATH=/app/logs — directory for storing logs.
  
* wait-for-selenium.sh ensures tests don’t start before Selenium server is ready.

* Logs are mounted as a volume to ./logs on host, so you can access test logs outside the container.

* Keep your local repository updated with remote branches (git pull) to avoid conflicts.
# Test CI/CD trigger