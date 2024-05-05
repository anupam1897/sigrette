pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/anupam1897/sigrette.git'
            }
        }
        stage('Installing Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps{
                sh 'echo "Automated Testing: PyTest"'
                sh 'python -m pytest'
            }
            
        }
        stage('Build') {
            steps {
                sh 'python setup.py build'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "To be deployed on varcel"'
                sh 'echo "Pipeline Ends Here"'
            }
        }
    }
}