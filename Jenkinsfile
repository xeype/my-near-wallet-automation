pipeline {
    agent any

    environment {
        ALLURE_RESULTS_DIR = '/var/lib/jenkins/workspace/mnw-auto/allure-results'
        ALLURE_REPORT_DIR = '/var/lib/jenkins/workspace/mnw-auto/allure-report'
        ACCOUNT_ID_1 = credentials('ACCOUNT_ID_1')
        ACCOUNT_ID_2 = credentials('ACCOUNT_ID_2')
        ACCOUNT_PASSWORD_1 = credentials('ACCOUNT_PASSWORD_1')
        ACCOUNT_PASSWORD_2 = credentials('ACCOUNT_PASSWORD_2')
        ACCOUNT_PASSPHRASE_1 = credentials('ACCOUNT_PASSPHRASE_1')
        ACCOUNT_PASSPHRASE_2 = credentials('ACCOUNT_PASSPHRASE_2')
        ACCOUNT_PK_1 = credentials('ACCOUNT_PK_1')
        ACCOUNT_PK_2 = credentials('ACCOUNT_PK_2')
    }

    parameters {
        string(name: 'TEST_SOURCE', defaultValue: 'tests', description: 'Directory for tests')
    }

    stages {
        stage('Clone repository') {
            steps {
                script {
                    checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/xeype/my-near-wallet-automation.git']]])
                }
            }
        }

        stage('Prepare Environment') {
            steps {
                script {
                    sh "mkdir -p ${ALLURE_RESULTS_DIR}"
                }
            }
        }

        stage('Clean Allure Results') {
            steps {
                script {
                    sh """
                    #!/bin/bash
                    rm -rf ${ALLURE_RESULTS_DIR}/*
                    """
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh """
                    #!/bin/bash
                    docker build --build-arg TEST_SOURCE=${params.TEST_SOURCE} \
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
                    """
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'docker run --rm -v ${ALLURE_RESULTS_DIR}:/app/allure-results my-python-tests'
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                script {
                    sh 'allure generate ${ALLURE_RESULTS_DIR} --clean -o ${ALLURE_REPORT_DIR}'
                }
            }
        }
    }

    post {
        always {
            allure includeProperties: false, jdk: '', reportBuildPolicy: 'ALWAYS', results: [[path: "${ALLURE_RESULTS_DIR}"]]
        }
    }
}
