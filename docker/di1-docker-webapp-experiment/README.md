# Di1 – Docker Webapp Experiment (Lab 6.2.7)

## Beschrijving
Dit project werd uitgevoerd in het kader van het vak **DevOps** en is gebaseerd op **Lab 6.2.7 – Build a Sample Web App in a Docker Container** (Cisco NetAcad).

Het doel van dit experiment is het ontwikkelen en containeriseren van een eenvoudige **Python Flask webapplicatie** met behulp van **Docker**.  
De webapp toont dynamisch het IP-adres van de client die de webpagina bezoekt.

---

## Projectstructuur

di1-docker-webapp-experiment/
├── sample_app.py
├── sample-app.sh
├── README.md
├── templates/
│ └── index.html
└── static/
└── style.css

yaml
Code kopiëren

> De map `tempdir/` wordt automatisch aangemaakt door het bash-script en wordt gebruikt als tijdelijke Docker build context.

---

## Gebruikte technologieën
- Python 3.8
- Flask
- Docker
- Bash scripting
- HTML & CSS
- Visual Studio Code
- DEVASC Virtual Machine

---

## Functionaliteit
- Een Flask webapp luistert op poort **8080**
- HTML en CSS worden geladen via Flask templates
- De webpagina toont dynamisch het IP-adres van de client
- Een bash-script automatiseert:
  - het aanmaken van mappen
  - het genereren van een Dockerfile
  - het bouwen van een Docker image
  - het starten van een Docker container

De webapp is bereikbaar via:
http://localhost:8080

yaml
Code kopiëren

---

## Uitvoeren van het project

### 1. Script uitvoerbaar maken

chmod a+x sample-app.sh

### 2. Docker image bouwen en container starten

Code kopiëren
./sample-app.sh

### 3. Webapp testen
Via de command line:

curl http://localhost:8080

Of via de browser:

Code kopiëren
http://localhost:8080