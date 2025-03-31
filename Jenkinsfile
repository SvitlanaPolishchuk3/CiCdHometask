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
					if [ -d "/tmp/jenkins_venv" ]; then
						rm -rf /tmp/jenkins_venv  
					fi

					python3 -m venv /tmp/jenkins_venv
					chmod -R 777 /tmp/jenkins_venv

					. /tmp/jenkins_venv/bin/activate
					pip install --upgrade --user pip
					pip install --user -r requirements.txt
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
