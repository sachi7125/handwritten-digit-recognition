pipeline {
    agent any

    stages {
        stage('Test in Python Container') {
            steps {
                sh '''
                docker run --rm \
                -v /Users/sachijain/Desktop/handwritten-digit-recognition:/app \
                -w /app \
                python:3.10-slim \
                bash -c "ls && pip install -r requirements.txt && PYTHONPATH=. pytest -q"
                '''
            }
        }
    }
}