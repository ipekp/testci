pipeline {
    agent any
    stages {
        stage('Setup python') {
            steps {
                script {
                    sh "python3 -m venv venv"
                    sh '''
                    . venv/bin/activate
                    pip3 install -r requirements.txt
                    '''
                }
            }
        }
        stage('Configure OSPF') {
            steps {
                script {
                    sh '''
                    . venv/bin/activate
                    python 01-netconf/configure-ospf.py
                    '''
                }
            }
        }
        stage('Test OSPF') {
            steps {
                script {
                    sh '''
                    . venv/bin/activate
                    python 01-netconf/test-ospf.py
                    '''
                }
            }
        }
    }
}
