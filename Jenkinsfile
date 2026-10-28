pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Install') {
            steps { sh 'pip install -r requirements.txt' }
        }
        stage('Test') {
            steps { sh 'pytest' }
        }
        stage('Lint') {
            steps { sh 'pip install flake8 && flake8 app.py' }
        }
    }
}