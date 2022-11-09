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

## Démarrer l'application

Pour lancer l'application en local sur http://127.0.0.1:5000
:
```sh
flask --app main --debug run
```

## Informations sur le projet
### Structure
Le project contient :
- un dossier pour le _code_ - "**main**"
- un dossier pour les _tests_ - "**test**"
- un dossier pour l'_environnement virtuel_ - "**venv**"
- un fichier **requirements.txt** pour _retenir les librairies_ 

Main est constitué d' :
- un dossier par **sujet** (book, user, chat,...) qui contient un dossier :
  - **controller** qui contient les classes qui auront une fonction par "_endpoint_" ou point d'entrée (REST)
  - **service** qui contient les classes services qui contiennent notre _logique_ et qui seront appeler par nos endpoints
  - **repository** qui contient les classes en _relation avec la base de données_ (POSTGRESQL)

### Fonctionnement
- Le fichier **\_\_init__.py** permet de _créer une application flask_, cette application peut avoir une configuration
- Le fichier **config.py** contient la _configuration de l'application_
- Les fichiers de type "**controller**" contiennent nos endpoints, _points d'entrées_ de notre application, qualifié par :
  - une **methode HTTP** (GET, POST, PUT, DELETE)
  - un **chemin relatif** à l'URL de base (exemple : "/book")
- Les fichiers de type "**service**" contiennent notre _logique_ (vérification et manipulation des données)
- Les fichiers de type "**repository**" contiennent nos _opérations sur la base de données_ (idéalment nous utiliserons un ORM)