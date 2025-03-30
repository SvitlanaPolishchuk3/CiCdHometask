pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    sh '''
                    if [ ! -d "/tmp/jenkins_venv" ]; then
                        python3 -m venv /tmp/jenkins_venv
                    fi

                    . /tmp/jenkins_venv/bin/activate
                    pip install --upgrade pip
                    pip install pytest
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh '''
                    . /tmp/jenkins_venv/bin/activate
                    pytest PyTests_1.py
                    '''
                }
            }
        }
    }
}
