pipeline {
    agent { dockerfile true }
    stages {
        stage('Composer install') {
            steps {
               echo "Composer install..."
            }
        }
        stage('Create .env') {
            environment {
                DB_CREDENTIALS = credentials('DB-JUKEBOX')
                DB_HOST = credentials('DB-JUKEBOX-HOST')
                DB_NAME = credentials('DB-JUKEBOX-NAME')
                DB_PORT = credentials('DB-JUKEBOX-PORT')
            }
            steps {
                writeFile file: '.env', text:
'''DB_ENV="testing_remote"

testing_remote_host="''' + env.DB_HOST + '''"
testing_remote_name="''' + env.DB_NAME + '''"
testing_remote_user="''' + env.DB_CREDENTIALS_USR + '''"
testing_remote_pass="''' + env.DB_CREDENTIALS_PSW + '''"
testing_remote_port="''' + env.DB_PORT + '''"

DB_HOSTNAME="${${DB_ENV}_host}"
DB_DATABASE="${${DB_ENV}_name}"
DB_USERNAME="${${DB_ENV}_user}"
DB_PASSWORD="${${DB_ENV}_pass}"
DB_PORT="${${DB_ENV}_port}"'''

                sh 'cat .env'
            }
        }
        stage('Fetch Google Ads Data') {
            steps {
                echo "Fetching Google Ads Data..."
            }
        }
    }
}