pipeline {
    agent any
    stages {
        stage('Setup Environment') {
            steps {
                /*sh 'chromedriver --version || true'
                sh 'google-chrome --version || true'
                sh 'which google-chrome || true'
                sh 'which chromedriver || true'*/
                sh '''
                bash -c "
                python3 -m venv venv
                source venv/bin/activate
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                playwright install
                "
                '''
            }
        }
        stage('Build') {
            steps {
                echo 'Building application...'
            }
        }

        stage('Test') {
            steps {
                sh '''
                bash -c "
                source venv/bin/activate
                pytest PlaywrightPython/test_web_api.py -v -s
                "
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
            }
        }
    }
}
