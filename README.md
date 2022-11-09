# Prérequis
Version de python : 3.8.10
- https://www.python.org/downloads/windows/

## Environnement virtuel
### Creation de l'environnement virtuel :
```sh
python3 -m venv ./venv
```

### Activation de l'environnement virtuel :
```sh
./venv/Scripts/activate
```

## Gestion des librairies
### Mettre à jour les librairies
> Attention à faire dans une fois l'environnement virtuel activer
```sh
pip install -r requirements.txt
```
### Mettre à jour requirements.txt

```sh
pip freeze > requirements.txt
```

## Informations sur le projet
### Structure
Le project contient :
- un dossier pour le _code_ - "**main**"
- un dossier pour les _tests_ - "**test**"
- un dossier pour l'_environnement virtuel_ - "**venv**"
- un fichier **requirements.txt** pour _retenir les librairies_

### Fonctionnement
- Le fichier **\_\_init__.py** permet de _créer une application flask_, cette application peut avoir une configuration
- Le fichier **config.py** contient la _configuration de l'application_