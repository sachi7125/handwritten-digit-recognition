pipeline {
    agent any

    stages {
        stage('Test in Python Container') {
            steps {
                sh '''
                echo "pip install -r requirements.txt" > run_tests.sh
                echo "PYTHONPATH=. pytest -q" >> run_tests.sh
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