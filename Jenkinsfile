pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/anupam1897/sigrette.git'
            }
        }
        stage('Build') {
            steps {
                echo "Doesn't require build. Prepare for Execution"
                pip install -r requirements.txt
            }
        }
        stage('Test') {
            steps {
                echo "Automated Testing: PyTest"
                python -m pytest
            }
        }
    }
}