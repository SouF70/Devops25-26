# Di2 – Eigen image-experiment (web service)

## Beschrijving
Dit project werd uitgevoerd in het kader van het vak **DevOps** en vormt het experiment **Di2 – Eigen image-experiment (web service)**.

In dit experiment werd een eenvoudige **Flask-gebaseerde webservice** ontwikkeld en gedeployed als een **Docker image**.  
De webservice levert een HTML-pagina die dynamisch het IP-adres van de client weergeeft.

Dit experiment is gebaseerd op de voorbeelden en richtlijnen uit de docentpresentatie rond Docker en microservices.

---

## Gebruikte technologieën
- Python 3.8
- Flask
- Docker
- HTML & CSS
- Visual Studio Code
- DEVASC Virtual Machine

---

## Functionaliteit
- De Flask webservice luistert op poort **5050**
- HTML en CSS worden geladen via Flask templates
- De webpagina toont dynamisch het IP-adres van de client
- De applicatie wordt volledig geïsoleerd uitgevoerd in een Docker container

De webservice is bereikbaar via:
http://localhost:5050


---

## Docker image bouwen

docker build -t di2-webservice-image .

## Docker container starten

docker run -d -p 5050:5050 --name di2-webservice-container di2-webservice-image