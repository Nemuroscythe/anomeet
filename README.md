
## Démarrer l'application

Pour lancer l'application sur http://127.0.0.1:5000
:
```sh
flask --app main --debug run
```
## Gestion des librairies
### Mettre à jour les librairies

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