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
          sh ' docker run -t anreddy/docker_compose_polls python3 ./mysite/manage.py test run'
            }
          }

       stage('Deploy') {
         steps {
            sh ' chmod 777 * '
            sshagent(credentials : ['ec2-user'])
            {
            sh 'ssh -o StrictHostKeyChecking=no ec2-user@10.0.2.119 uptime'
            sh 'ssh -v ec2-user@10.0.2.119'
            sh 'scp * ec2-user@10.0.2.119:/home'
            sh 'ssh ec2-user@10.0.2.119 docker-compose up --build  -d '
            }
            }
         }
       }
     }







