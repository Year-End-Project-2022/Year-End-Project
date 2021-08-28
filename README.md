# site du Lab

Bienvenu sur le dépôt gitlab du site internet du labouest le fablab de la roche sur yon

L'idée est de crées un ensemble d'outils pour automatisé centraliser et aider la gestion du lieu a travers sont site internet

un des premier objectif et de crée un formulaire pour l'invertaire d'outils présent dans le lieux

par la suite on peut crée un autre formulaire pour les fraise des CNC

on pourrait aussi faire le site du lab

pour faire fonctionné le projet en local il faut faire un venv pip avec les `requirements.txt` et les `localrequirement.txt` d'installé
il faut aussi définire une variable d'environement : `DEBUG` a true pour que le debug et les host soit correctement activé

la secrete key est généré automatiquement

pour run le serveur tout se fait avec le fichier `manage.py`
la 1er fois il faut lancer la commande `./manage.py createsuperuser` pour crées un admin
puis faire `./manage.py makemigrations` et `./manage.py migrate` pour crée les migrations et les appliquer a la base de donnée _(en gros sa crées les table)_

pour finir lancer le serveur avec la commande `./manage.py runserver`

Le projet tourne aussi avec docker il faut avoir `docker` et `docker-compose` d'installer et fonctionnel pour le faire fonctionner avec.

Le `docker-compose.yml` sert pour le développement il utilise la base sqlite par défaut n'a pas de proxy et fonctionne avec le debug activer

Le `docker-compose-deploy.yml` sert lui a la mise en production il faut tournée l'application sans le debug utilise le proxy ngnix et une base de donnée postgress

# l'arborescence:

## dossier :

- `app` contient les fichier source

- `proxy` contient les fichier de config de nginx

- `.githooks` contient les hooks a lancer avant chaque commit pour évité l'ajout de bug et monitor le niveau de test de l'application

- `script` contient le script de lancement de la docker de django

## les fichier :

- `.gitignore` (fait sur [gitignore.io](https://www.toptal.com/developers/gitignore) ) et `.prettignore` sont des fichiers pour git et prettier pour leur dire quel fichier ignoré

- `.gitlab-ci.yml` est le fichier de config des pipeline gitlab

- `Dockerfile` est le fichier de config de la docker django

- `setup.cfg` est le fichier de config utiliser par coverage

- `localrequirement.txt` est l'ensemble des outils utiliser en local pour tester le code (prospector,bandit,coverage) utiliser pour les pré-commits
