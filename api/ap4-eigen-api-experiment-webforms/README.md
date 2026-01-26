# AP4 – Eigen API-experiment (Webforms)

## Doel
Dit experiment demonstreert het gebruik van een externe REST API
via Python, zoals behandeld in Presentation 2 – API Calls.

Met behulp van een webformulier kan een gebruiker een vertrekplaats
en bestemming ingeven, waarna de route, afstand en reistijd worden
berekend via de GraphHopper API.

## Gebruikte technologieën
- Python 3
- Flask
- HTML (webform)
- GraphHopper REST API

## Werking
1. De gebruiker vult een vertrekplaats en bestemming in.
2. Het formulier stuurt de gegevens via POST naar de Flask-app.
3. De Flask-app roept de GraphHopper API aan.
4. Afstand en reistijd worden berekend en getoond in de browser.

## Uitvoering
Start de applicatie met:

python3 app.py