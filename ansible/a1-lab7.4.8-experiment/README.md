# A1 – Lab 7.4.8 Ansible experiment

## Context
Dit experiment werd uitgevoerd in het kader van het vak  
DevOps.

## Beschrijving
In dit lab werd Ansible gebruikt om de installatie en configuratie
van een Apache webserver te automatiseren. De communicatie met de
webserver gebeurt via SSH op een gesimuleerde host binnen de
DEVASC virtuele machine.

## Gebruikte technieken
- Ansible
- Inventory (hosts)
- Playbooks
- SSH
- Ansible modules: ping, command, apt, service
- Handlers

## Uitvoering
De playbooks werden uitgevoerd met het volgende commando:

ansible-playbook install_apache_playbook.yaml

## Resultaat

De Apache webserver werd succesvol geïnstalleerd en gestart.
De webserver is bereikbaar via de browser op het IP-adres 192.0.2.3
en toont de standaard Apache2 Ubuntu webpagina.
