pipeline {
    agent any

    environment {
        PYTHON = '/Svitlana_Polishchuk/bin/python3'  
    }

    stages {
        stage('Clone Repository') {
            steps {
                checkout([
                    $class: 'GitSCM', 
                    branches: [[name: '*/main']], 
                    userRemoteConfigs: [[url: 'https://github.com/SvitlanaPolishchuk3/CiCdHometask']]
                ])
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }

        stage('Create Develop Branch') {
            steps {
                script {
                    sh "git checkout -b develop || git checkout develop"
                    sh "git push origin develop"
                }
            }
        }

        stage('Deploy to Release Branch') {
            when {
                branch 'develop'  // Only run when pushing to 'develop'
            }
            steps {
                script {
                    sh "git checkout -b release || git checkout release"
                    sh "git merge develop"
                    sh "git push origin release"
                }
            }
        }
    }
}