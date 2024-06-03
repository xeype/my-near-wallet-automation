pipeline {
    agent any

    environment {
        ALLURE_RESULTS_DIR = 'allure-results'
        ALLURE_REPORT_DIR = 'allure-report'
    }

    stages {
        stage('Clone repository') {
            steps {
                script {
                    checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/xeype/my-near-wallet-automation.git']]])
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t my-python-tests .'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'docker run --rm -v ${WORKSPACE}/${ALLURE_RESULTS_DIR}:/app/allure-results my-python-tests'
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
