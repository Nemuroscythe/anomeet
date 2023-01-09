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
> Attention à faire une fois l'environnement virtuel activé
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
Exécuter le fichier contenant "application.run", ici :
anomeet_backend.py

## Lancer les tests pytest
>A noter que pytest reconnait uniquement les _fichiers_ avec **\_test** et les _fonctions_ commencant par **test_** 
```sh
python -m pytest
```


## Informations sur le projet
### Structure

### Fonctionnement
