pipeline {
    agent any
     environment {
        DOCKER_CREDS=credentials('docker_id')
        }
     stages {

       stage ('Build') {
         steps {
          sh 'docker build -t anreddy/docker_compose_polls . '
             }
          }

       stage ('Test'){
         steps {
          sh ' docker run -t anreddy/docker_compose_polls python ./mysite/manage.py test run'
            }
          }

       stage('Deploy') {
         steps {

            sh 'docker-compose up '

           }
         }
       }
        }







