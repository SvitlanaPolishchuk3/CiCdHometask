pipeline {
    agent any

    environment {
        PYTHON = '/Svitlana_Polishchuk/bin/python3'  // Adjust based on Docker
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip install -r requirements.txt || echo "Failed to install dependencies!"'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh 'pytest tests/ || echo "Tests failed!"'
            }
        }
    }
}
