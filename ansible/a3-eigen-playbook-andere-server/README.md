# A3 – Eigen Ansible playbook (andere server)

## Context
Dit experiment werd uitgevoerd in het kader van het vak DevOps 
en is gebaseerd op Presentation 6 – Configuration Management & Ansible.

## Beschrijving
In dit experiment werd met Ansible een Apache webserver geconfigureerd
op een andere host dan de standaard server.
De webserver luistert op een aangepaste poort (8082) en toont een
custom HTML-pagina.

## Gebruikte configuratie
- Target server: 192.0.2.4
- Webserver: Apache2
- Poort: 8082
- Configuratie via Ansible playbook
- Webpagina automatisch gedeployed

## Gebruikte technieken
- Ansible inventory (hosts)
- Ansible playbook (YAML)
- Modules:
  - apt
  - lineinfile
  - copy
  - service
- Handlers voor herstarten van Apache
- Apache VirtualHost configuratie

## Uitvoering
Het playbook werd uitgevoerd met:

ansible-playbook a3_custom_webserver.yaml
