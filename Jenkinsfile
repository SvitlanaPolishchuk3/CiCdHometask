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
                    echo "Setting up Python virtual environment..."
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
                    echo "Running tests..."
                    . venv/bin/activate  
                    pytest --junitxml=pytest_report.xml PyTests_1.py
                    '''
                }
            }
        }

        stage('Release Deployment') {
            steps {
                script {
                    sh '''
                    echo "Creating release branch and pushing changes..."
                    git checkout -b release
                    git push origin release
                    '''
                }
            }
        }
    }

    post {
        always {
            junit 'pytest_report.xml'
        }
    }
}
