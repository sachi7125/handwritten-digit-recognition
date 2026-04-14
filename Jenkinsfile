pipeline {
    agent any

    stages {
        stage('Test in Python Container') {
            steps {
                sh '''
                docker run --rm \
                -v $WORKSPACE:/app \
                -w /app \
                python:3.10-slim \
                sh -c "pip install -r requirements.txt && PYTHONPATH=. pytest -q"
                '''
            }
        }
    }
}