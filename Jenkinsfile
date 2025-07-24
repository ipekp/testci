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
        stage('NETCONF: Configure OSPF') {
            steps {
                script {
                    sh '''
                    . venv/bin/activate
                    python 01-netconf/configure-ospf.py
                    '''
                }
            }
        }
        stage('NETCONF: Test OSPF') {
            steps {
                script {
                    sh '''
                    . venv/bin/activate
                    python 01-netconf/test-ospf.py
                    '''
                }
            }
        }

        stage('RESTCONF: Init') {
            steps {
                script {
                    sh '''
                    . venv/bin/activate
                    python 02-restconf/init-ospf.py
                    '''
                }
            }
        }
        stage('RESTCONF: Configure OSPF') {
            steps {
                script {
                    sh '''
                    . venv/bin/activate
                    python 02-restconf/configure-ospf.py
                    '''
                }
            }
        }
        stage('RESTCONF: Test OSPF') {
            steps {
                script {
                    sh '''
                    . venv/bin/activate
                    python 02-restconf/test-ospf.py
                    '''
                }
            }
        }
        stage('Ansible: configure BGP') {
            steps {
                sh '''
                . venv/bin/activate
                ansible-playbook -i inventory configure.yaml"
                '''
            }
        }
        stage('Ansible: test BGP') {
            steps {
                sh '''
                . venv/bin/activate
                ansible-playbook -i inventory test.yaml"
                '''
            }
        }
    }
}
