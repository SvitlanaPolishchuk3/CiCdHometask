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
					VENV_DIR="venv"

					if [ -d "$VENV_DIR" ]; then
						rm -rf "$VENV_DIR"
					fi

					python3 -m venv "$VENV_DIR"
					. "$VENV_DIR/bin/activate"
					pip install --upgrade pip
					pip install -r requirements.txt
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
