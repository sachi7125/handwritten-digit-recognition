pipeline {
    agent any

    stages {
        stage('Install') {
            steps {
                sh '''
                apt-get update
                apt-get install -y python3-pip
                pip3 install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh 'PYTHONPATH=. pytest -q'
            }
        }
    }
}