pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/SvitlanaPolishchuk3/CiCdHometask.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the project...'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'pip install -r requirements.txt || true'  // Install dependencies if a requirements.txt exists
                sh 'pytest PyTests_1.py'  // Run your pytest script
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
            }
        }
    }
}