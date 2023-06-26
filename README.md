# RaspHome

## Présentation

Logiciel personnalisé pour un Raspberry Pi 4

Il est conçu pour être affiché sur un écran tactile 7 pouces (640x480)

## Installation

Installer les packages nécessaires :
```bash
sudo apt-get install python3-pip
pip install cusromtkinter
pip install requests
```

Créer un fichier `config.py` dans le dossier `api`.
Ce fichier stocke les différentes clés API.
Puis y ajouter ces lignes en remplaçant les valeurs `<>` :
```python
# https://weatherstack.com/
WEATHER_STACK_API_KEY="<API_KEY>"
WEATHER_STACK_CITY="<CITY>"
```

## Fonctionnalités
- Affichage de l'heure et de la date
- Affichage de la température et de l'humidité grâce à un capteur DHT22
- Luminosité variable grâce à une photorésistance GL5539

## Améliorations potentielles
- Ajout d'un réveil
- Affichage du débit Internet
- Affichage d'informations concernant un futur cloud
- Affichage de statistiques
- Affichage des anniversaires
- Affichage de la météo / température extérieure