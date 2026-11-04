pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Install') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Lint') {
            steps {
                sh '''
                    . .venv/bin/activate
                    flake8 app.py
                '''
            }
        }
        stage('Unit Test') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pytest
                '''
            }
        }
    }
}