#!/bin/bash

# Maak tijdelijke mappen
mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static

# Kopieer bestanden naar tempdir
cp sample_app.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

# Dockerfile aanmaken
echo "FROM python:3.8-slim" > tempdir/Dockerfile
echo "RUN pip install flask --no-cache-dir --progress-bar off" >> tempdir/Dockerfile
echo "COPY ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY sample_app.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 8080" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/sample_app.py" >> tempdir/Dockerfile

# Docker image bouwen
cd tempdir
docker build -t sampleapp .

# Container starten
docker run -t -d -p 8080:8080 --name samplerunning sampleapp

# Containers tonen
docker ps -a