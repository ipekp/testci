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
    }
}
