pipeline {
    agent any

    stages {
        stage('Install') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'PYTHONPATH=. pytest -q'
            }
        }

        stage('Build Docker') {
            steps {
                sh 'docker build -t digit-recognizer .'
            }
        }
    }
}