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

                cp .env.sample .env

                sed -i 's/development_host="db.host.name"/development_host="host.docker.internal"/g' .env
                sed -i 's/development_name="db_name"/development_name="fastCRM_local"/g' .env
                sed -i "s/development_user=\"db_username\"/development_user=\"test\"/g" .env
                sed -i "s/development_pass=\"db_password\"/development_pass=\"test\"/g" .env
                sed -i 's/development_port="db_port"/development_port="3306"/g' .env

                cat .env
                '''
            }
        }
    }
}
