pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            environment {
                DB_LOCAL = credentials('DB-LOCAL')
            }
            steps {
                sh '''
                php -v
                pwd
                ls -liah
                composer -V
                echo "Credentials: $DB_LOCAL"
                echo "DB User is $DB_LOCAL_USR"
                echo "DB Pass is $DB_LOCAL_PSW"
                '''
                writeFile file: '.env', text: 'test text
                new line

                DB_USERNAME="\${\${DB_ENV}_user}"'
                sh '''
                cat .env
                '''
            }
        }
    }
}
