pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout your code from the repository
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

                    
                    source /tmp/jenkins_venv/bin/activate
                    pip install --upgrade pip  
                    pip install pytest  
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Activate virtual environment and run PyTests_1.py
                    sh '''
                    source /tmp/jenkins_venv/bin/activate  
                    pytest PyTests_1.py  
                    '''
                }
            }
        }
    }
}
