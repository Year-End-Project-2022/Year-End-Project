# Site internet Lab Ouest

Lancement de l'application en local :


0/ Se positionner dans /app_python/
1/ ajouter la variable d'environnement DEBUG=1
2/ Python migrate pour la base de donnée
3/ Créer un superuser pour accéder à la partie admin
4/ Lancer le serveur

export DEBUG=1
./app/manage.py migrate 
./app/manage.py createsuperuser
./app/manage.py runserver

Accessible à http://127.0.0.1:8000

Lancement de l'application via docker : 

0/ Se positionner dans /app_python/
1/ Remplir un .env tel que :
DB_NAME=postgres
DB_USER=postgres
DB_PASS=
SECRET_KEY=
ALLOWED_HOSTS=localhost,*

2/ Lancer le docker-compose-deploy
3/ faire un docker exec sur le conteneur de l'application pour la création d'un superuser

docker-compose -f docker-compose-deploy up --build
docker exec -it app_python_app_1 ./manage.py createsuperuser

Accessible à http://0.0.0.0

Déploiement de l'application sur un serveur distant via ansible + docker :

1/ Il faut également ajouter un .env dans /app_python/ tel que précedement.
2/ Se positionner dans /ansible/
3/ Modifier le fichier hosts avec les informations de votre machine distante. (IP, USER & MDP)
4/ Lancer le playbook.

ansible-playbook -i hosts playbook.yml

Accessible à http://[IP_DISTANTE]






