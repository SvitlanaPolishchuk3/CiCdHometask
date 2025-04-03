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
                withCredentials([usernamePassword(credentialsId: 'github-pat', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD')]) {
                    script {
                        sh '''
                        echo "Configuring Git credentials..."
                        git config --global credential.helper store
                        echo "https://$GIT_USERNAME:$GIT_PASSWORD@github.com" > ~/.git-credentials
                        git config --global credential.useHttpPath true

                        echo "Creating release branch and pushing changes..."
                        git checkout -b release
                        git push origin release

                        # Cleanup for security
                        rm -f ~/.git-credentials
                        git config --global --unset credential.helper
                        '''
                    }
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
