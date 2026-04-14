pipeline {
    agent any

    stages {
        stage('Install & Test') {
            steps {
                sh '''
                docker run --rm \
                -v $(pwd):/app \
                -w /app \
                python:3.10-slim \
                sh -c "pip install -r requirements.txt && PYTHONPATH=. pytest -q"
                '''
            }
        }

        stage('Build Docker') {
            steps {
                sh 'docker build -t digit-recognizer .'
            }
        }
    }
}