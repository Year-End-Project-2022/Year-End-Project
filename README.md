# Site internet Lab Ouest

Lancement de l'application en local :
---------------------

0/ Se positionner dans /app_python/ <br>
1/ ajouter la variable d'environnement DEBUG=1 <br>
2/ Python migrate pour la base de donnée <br>
3/ Créer un superuser pour accéder à la partie admin<br>
4/ Lancer le serveur <br>

`export DEBUG=1`
<br>
`./app/manage.py migrate`
<br>
`./app/manage.py createsuperuser`
<br>
`./app/manage.py runserver`

Accessible à http://127.0.0.1:8000
Partie admin accessible à http://127.0.0.1:8000/admin

Lancement de l'application via docker : 
---------------------

0/ Se positionner dans /app_python/<br>
1/ Remplir un .env tel que : <br>
`DB_NAME=postgres`<br>
`DB_USER=postgres`<br>
`DB_PASS=`<br>
`SECRET_KEY=`<br>
`ALLOWED_HOSTS=localhost,*`<br>

2/ Lancer le docker-compose-deploy
3/ faire un docker exec sur le conteneur de l'application pour la création d'un superuser

`docker-compose -f docker-compose-deploy up --build`
<br>
`docker exec -it app_python_app_1 ./manage.py createsuperuser`

Accessible à http://0.0.0.0
Partie admin accessible à http://0.0.0.0/admin

Déploiement de l'application sur un serveur distant via ansible + docker :
---------------------

1/ Il faut également ajouter un .env dans /app_python/ tel que précedement.<br>
2/ Se positionner dans /ansible/ <br>
3/ Modifier le fichier hosts avec les informations de votre machine distante. (IP, USER & MDP) <br>
4/ Lancer le playbook.<br>

`ansible-playbook -i hosts playbook.yml`

Accessible à http://[IP_DISTANTE]
Partie admin accessible à http://[IP_DISTANTE]/admin





