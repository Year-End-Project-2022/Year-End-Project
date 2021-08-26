# site du Lab

premier objectif et de crée un formulaire pour l'invertaire d'outils

par la suite on peut crée un autre formulaire pour les fraise des CNC

on pourrait aussi faire le site du lab

pour faire fonctionné le projet en local il faut faire un venv pip avec les `requirements.txt` et les `localrequirement.txt` d'installé
il faut aussi définire une variable d'environement : `DJANGO_DEBUG` a true pour que le debug et les host soit correctement activé

la secrete key est généré automatiquement la 1er foit et est stocké dans le fichier `secrets.json` qui n'est pas versionné

pour run le serveur tout se fait avec le fichier `manage.py`
la 1er fois il faut lancer la commande `./manage.py createsuperuser` pour crées un admin
puis faire `./manage.py makemigrations` et `./manage.py migrate` pour crée les migrations et les appliquer a la base de donnée _(en gros sa crées les table)_

pour finir lancer le serveur avec la commande `./manage.py runserver`
