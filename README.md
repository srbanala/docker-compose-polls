# docker-compose-polls
This repository used for docker stack deployment method.

File based environment variables can be passed for postgres username and password using below method
secrets:
 postgres-user:
   file: /secrets/user_filename.txt
 postgres-password: 
   file: /secrets/password_filename.txt

command for creating secrets in docker from command line.
echo "postgres"|docker secret create postgres-user -
echo "welcome1"|docker secret create postgres-password -

Commands for creating secrets in docker using files.

docker secret create postgres-user filename



