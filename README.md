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

Create a Python virtual environment locally:

```bash
pip install virtualenv
```
```bash
py -3.11 -m venv venv
```
```bash
venv\Scripts\activate
```
```bash
pip install -r requirements.txt
```

## Test Framework Configuration and Setup
We use pip-tools to manage dependencies and generate requirements.txt.

Main Python packages used
* pytest — test runner

* selenium — for UI web testing

* webdriver-manager — auto-manages browser drivers

* loguru — for logging

* requests — HTTP requests

* Faker — test data generation

Install all dependencies using:
```bash
pip install -r requirements.txt
```

## Running Tests Locally
Run tests without allure reports :
```bash
pytest tests/
```

Run tests from allure reports and clearing old reports
Run tests without allure reports :
```bash
 .\run_tests_allure.ps1
```

To view Allure reports
```bash
allure serve ./allure-results
```

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
1. Ensure Docker and Docker Compose are installed and running.
2. From project root, run:
```bash
docker-compose up --build --abort-on-container-exit
```
3. The tests container waits for Selenium to be ready and then runs the tests automatically.
4. Logs will be saved in the logs/ directory on the host machine.

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