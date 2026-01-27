# Dm1 – Docker management-experiment

## Beschrijving
In dit experiment werd het beheer van Docker onderzocht. Er werd gewerkt met
Docker-commando’s om informatie op te vragen en resources te beheren zoals
containers, images en volumes.

## Docker informatie

docker info

### Images beheren
docker images
docker rmi nginx

### Containers beheren
docker ps -a
docker rm dc1-nginx-container

### Volumes beheren
docker volume ls
docker volume inspect di3-mysql-data
docker volume rm di3-mysql-data

### Systeem opruimen

docker system prune
docker system prune -a --volumes