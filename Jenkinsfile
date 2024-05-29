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
                sh '''
                cat <<EOF >.env
                DB_ENV="development"

                development_host="host.docker.internal"
                development_name="fastCRM_local"
                development_user=$DB_LOCAL_USR
                development_pass=$DB_LOCAL_PSW
                development_port="3306"
                EOF
                '''
                sh 'cat .env'
            }
        }
    }
}
