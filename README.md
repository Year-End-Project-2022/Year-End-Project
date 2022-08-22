# site du Lab

Bienvenue sur le dépôt gitlab du site internet du Labouest le fablab de la Roche-sur-Yon.

L'idée est de créer un ensemble d'outils pour automatiser, centraliser et aider à la gestion du lieu à travers son site internet.

Un des premier objectif et de créer un formulaire pour l'invertaire d'outils présents dans le lieux.

Par la suite on peut créer un autre formulaire pour les fraises des CNC

on pourrait aussi faire le site du lab

pour faire fonctionné le projet en local il faut faire un venv pip avec les `requirements.txt` et les `localrequirement.txt` d'installé
il faut aussi définire une variable d'environement : `DEBUG` a true pour que le debug et les host soit correctement activé

la secrete key est généré automatiquement

pour run le serveur tout se fait avec le fichier `manage.py`
la 1er fois il faut lancer la commande `./manage.py createsuperuser` pour crées un admin
puis faire `./manage.py makemigrations` et `./manage.py migrate` pour crée les migrations et les appliquer a la base de donnée _(en gros sa crées les table)_

pour finir lancer le serveur avec la commande `./manage.py runserver`

pour git les hooks son dans .githook (commande pour changé le chemin par defaut : `git config.core.hooksPath .githooks`)

Le projet tourne aussi avec docker il faut avoir `docker` et `docker-compose` d'installer et fonctionnel pour le faire fonctionner avec.

Le `docker-compose.yml` sert pour le développement il utilise la base sqlite par défaut n'a pas de proxy et fonctionne avec le debug activer

Le `docker-compose-deploy.yml` sert lui a la mise en production il faut tournée l'application sans le debug utilise le proxy ngnix et une base de donnée postgress

# l'arborescence:

## dossier :

-   `app` contient les fichier source

-   `proxy` contient les fichier de config de nginx

-   `.githooks` contient les hooks a lancer avant chaque commit pour évité l'ajout de bug et monitor le niveau de test de l'application

-   `script` contient le script de lancement de la docker de django

## les fichier :

-   `.gitignore` (fait sur [gitignore.io](https://www.toptal.com/developers/gitignore) ) et `.prettignore` sont des fichiers pour git et prettier pour leur dire quel fichier ignoré

-   `.gitlab-ci.yml` est le fichier de config des pipeline gitlab

-   `Dockerfile` est le fichier de config de la docker django

-   `setup.cfg` est le fichier de config utiliser par coverage

-   `localrequirement.txt` est l'ensemble des outils utiliser en local pour tester le code (prospector,bandit,coverage) utiliser pour les pré-commits

    # note pour les install

    pip3 install rotate-backups (a installer sur le serveur avec pip)

    (install crontables)

    /etc/crontab/

        0 0 \* \* 0 rotate-backups

    make /etc/rotate-backups.ini

    ```ini
    [/media/Labouest-backups]
    hourly = 24
    daily = 7
    weekly = 4
    monthly = 12
    yearly = always
    ionice = idle
    ```
