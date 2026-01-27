# Di3 – Eigen image-experiment 2 (SQL)

## Beschrijving
In dit experiment werd een eigen Docker image gebouwd voor een MySQL-database.
De database wordt automatisch geïnitialiseerd via een SQL-script en maakt gebruik
van Docker volumes om persistente data te garanderen.

## Bestanden
- Dockerfile
- init.sql

## Dockerfile
De image is gebaseerd op MySQL 5.7 om compatibiliteitsproblemen te vermijden.

## Image bouwen

docker build -t di3-mysql-image .

### Container starten
docker run -d \
  -p 3306:3306 \
  --name di3-mysql-container \
  -v di3-mysql-data:/var/lib/mysql \
  di3-mysql-image

### Database testen

docker exec -it di3-mysql-container mysql -u root -p

USE devopsdb;
SELECT * FROM users;