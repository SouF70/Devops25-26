# Dc1 – Run containers-experiment

## Beschrijving
In dit experiment werd een bestaande Docker image gebruikt om containers te starten,
stoppen en beheren. Hiervoor werd het officiële Nginx image gebruikt.

## Container starten

docker run -d -p 8081:80 --name dc1-nginx-container nginx

### Container testen
curl http://localhost:8081

### Container stoppen en starten

docker stop dc1-nginx-container
docker start dc1-nginx-container

### Logs bekijken
docker logs dc1-nginx-container

### Container inspecteren
docker inspect dc1-nginx-container