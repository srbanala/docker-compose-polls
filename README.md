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

######################## Docker Swarm commands#########

1.TO install docker swarm ,execute below command.
   docker swarm init

2. To add worker node to swarm cluster ,execute on leader nod
    docker swarm join --token

3. To add manager to this swarm,execute on leader node
   docker swarm join-token manager 



#######################################To install docker-compose ########################

 sudo curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-`uname -s`-`uname -m` | sudo tee /usr/local/bin/docker-compose > /dev/null
 sudo chmod +x /usr/local/bin/docker-compose
 sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose



