# my-near-wallet-automation Test Framework Setup

This guide will help you set up a my-near-wallet-automation test framework. Follow the steps below to get started.

## Table of Contents
0. [Prerequisites](#Prerequisites)
1. [Clone the Repository](#1-clone-the-repository)
2. [Create a Virtual Environment](#2-create-a-virtual-environment)
3. [Install Dependencies](#3-install-dependencies)
4. [Install ChromeDriver](#4-install-chromedriver)
5. [Configuration](#5-configuration)
6. [Running Tests](#6-running-tests)
7. [Generate Allure Reports](#7-generate-allure-reports)
8. [Docker Setup (Optional)](#8-docker-setup-optional)
    - [Build the Docker Image](#build-the-docker-image)
    - [Run the Docker container](#run-the-docker-container)


## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.8 <= version <= 3.10
- pip (Python package installer)
- Git
- Docker
- Chrome browser
- ChromeDriver
- wget

## 1. Clone the Repository

Clone the project repository from GitHub.

```bash
git clone https://github.com/your-repository.git
cd your-repository
````

## 2. Create a Virtual Environment
Create and activate a virtual environment to manage your project dependencies.
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\
```

## 3. Install dependencies
Install the required Python packages listed in the requirements.txt file.
```bash
pip install -r requirements.txt
```

## 4. Ensure that ChromeDriver is installed and available in your system's PATH

```bash
# Download ChromeDriver
wget -O /tmp/chromedriver_linux64.zip https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.141/linux64/chromedriver-linux64.zip
unzip /tmp/chromedriver_linux64.zip -d /usr/local/bin/
rm /tmp/chromedriver_linux64.zip

# Move ChromeDriver to /usr/local/bin
mv /usr/local/bin/chromedriver-linux64/chromedriver /usr/local/bin/
```

## 5. Configuration
Configure your test environment by setting the necessary environment variables. You can use a .env file or export variables directly in your terminal.

```bash
export TEST_SOURCE='tests'
export ACCOUNT_ID_1='your_account_id_1'
export ACCOUNT_ID_2='your_account_id_2'
export ACCOUNT_PASSWORD_1='your_account_password_1'
export ACCOUNT_PASSWORD_2='your_account_password_2'
export ACCOUNT_PASSPHRASE_1='your_account_passphrase_1'
export ACCOUNT_PASSPHRASE_2='your_account_passphrase_2'
export ACCOUNT_PK_1='your_account_pk_1'
export ACCOUNT_PK_2='your_account_pk_2'
```
## 6. Running tests
You can run your tests using Pytest. 
```bash
pytest tests
```
 - Also you can specify the path to test folder such as tests/ui/

To generate Allure reports, add the following argument:
```bash
--alluredir=allure-results
```

## 7. Generate Allure Reports
```bash
allure serve allure-results
```

## 8. Docker Setup (Optional)
If you prefer to run your tests inside a Docker container, follow these steps:
### Build the Docker Image
Build the Docker image with all needed arguments using the following command:
```bash
docker build --build-arg TEST_SOURCE=${TEST_SOURCE} \
                    --build-arg ACCOUNT_ID_1=${ACCOUNT_ID_1} \
                    --build-arg ACCOUNT_ID_2=${ACCOUNT_ID_2} \
                    --build-arg ACCOUNT_PASSWORD_1=${ACCOUNT_PASSWORD_1} \
                    --build-arg ACCOUNT_PASSWORD_2=${ACCOUNT_PASSWORD_2} \
                    --build-arg ACCOUNT_PASSPHRASE_1="${ACCOUNT_PASSPHRASE_1}" \
                    --build-arg ACCOUNT_PASSPHRASE_2="${ACCOUNT_PASSPHRASE_2}" \
                    --build-arg ACCOUNT_PK_1="${ACCOUNT_PK_1}" \
                    --build-arg ACCOUNT_PK_2="${ACCOUNT_PK_2}" \
                    -t my-python-tests \
                    .
```

### Run the Docker container
Specify the local path to results folder and run the following command: 
```bash
docker run --rm -v /local/results/path:/app/allure-results my-python-tests
```