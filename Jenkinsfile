pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                sh '''
                php -v
                pwd
                ls -liah
                composer -V
                '''
            }
        }
    }
}
