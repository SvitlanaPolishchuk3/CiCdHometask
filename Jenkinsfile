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
                        git remote set-url origin https://$GIT_USERNAME:$GIT_PASSWORD@github.com/CiCdHometask.git

                        echo "Checking if 'release' branch exists..."
                        if git show-ref --quiet refs/heads/release; then
                            echo "'release' branch already exists. Checking it out..."
                            git checkout release
                        else
                            echo "Creating new 'release' branch..."
                            git checkout -b release
                        fi

                        echo "Pushing changes to the release branch..."
                        git push origin release
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
