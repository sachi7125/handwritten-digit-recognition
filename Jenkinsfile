pipeline {
    agent any

    stages {
        stage('Test in Python Container') {
            steps {
                writeFile file: 'run_tests.sh', text: '''#!/bin/sh
pip install -r requirements.txt
PYTHONPATH=. pytest -q
'''
                sh '''
                chmod +x run_tests.sh

                docker run --rm \
                -v $WORKSPACE:/app \
                -w /app \
                python:3.10-slim \
                sh /app/run_tests.sh
                '''
            }
        }
    }
}