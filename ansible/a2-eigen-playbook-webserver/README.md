# A2 – Eigen playbook-experiment (webserver)

## Context
Dit experiment werd uitgevoerd in het kader van het vak DevOps en is gebaseerd op  
Presentation 6 – Ansible Part Two.

## Beschrijving
In dit experiment werd een eigen Ansible-playbook ontwikkeld
om een Apache webserver automatisch te installeren,
configureren en voorzien van een aangepaste webpagina.

De configuratie wijzigt de standaard Apache-poort
en deployt een custom HTML-pagina via Ansible.

## Gebruikte technieken
- Ansible
- Inventory en ansible.cfg
- Playbooks
- Modules: apt, lineinfile, copy, service
- Handlers
- SSH-communicatie

## Uitvoering
Het playbook werd uitgevoerd met:

ansible-playbook a2_custom_webserver.yaml
