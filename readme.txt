	DEPLOIEMENT LOCAL DE L'APPLICATION PERSISTENT
	Mars 2015

Note: le vrai déploiement nécessite un véritable serveur ( linux + nginx (reverse proxy) + uwsgi (serveur applicatif) )

1) Installation des dépendances sous Windows (version 7):

  1.a) installation de PYTHON (version 3.4.3) :
	* installer l'application: https://www.python.org/downloads/release/python-343/
		note: laisser les options par défaut (il faut que les packages "pip" et "setuptools" soient installés).
	* configuration des variables d'environnement:
	- menu Démarrer, rechercher:"variables d'environnement"
	- dans la fenêtre qui s'ouvre ("propriétés systèmes") et dans l'onglet ("avancé"), cliquer sur "Variables d'environnnement"
	- dans la liste défilante inférieure, sélectionner la variable "Path", puis cliquer sur "Editer".
	- rajouter à la fin de la liste la chaîne suivante: ";C:\Python34;C:\Python43\Scripts", où "Python34" correspond au dossier où Python 3 a été installé
	- cliquer "Ok" puis "Appliquer".
	* vérification de l'installation: 
	- ouvrir un shell de commande (raccourci clavier: "touche windows+R", puis taper "cmd" et "Ok": 
	- exécuter dans le shell "python": une nouvelle invite (">>>") doit apparaître, où on peut exécuter du code python 
		(taper "quit()" ou "exit()" pour revenir au shell). (note: un raccourci pour stopper un processus dans le shell : "ctrl+c" )


  1.b) installation de DJANGO (version 1.7.7) : 
	- ouvrir un shell de commande, puis exécuter "pip install django==1.7.7"


2) Installation du projet:
	* copier le dossier "Source" dans le répertoire de votre choix (attention: ne rien y modifier!), si possible dans votre dossier d'utilisateur windows pour ne pas avoir à trop naviger dans le shell (plusieurs "cd")
	* vérification de l'installation: dans un shell, exécuter "python", puis dans le shell python qui s'affiche, exécuter successivement "import django", touche Entrée, puis "django.VERSION": la version de django devrait s'afficher.


3) Lancement de l'application:

  3.a) Lancement du serveur intégré à DJANGO (en écoute sur le port réseau 8000 )
	* lancer un shell, puis naviger (cd "nom du répertoire", ou 'cd .." pour revenir en arrière) jusqu'au répertoire "Source"
	* exécuter la commande "manage.py runserver"
	* IMPORTANT: laisser la fenêtre ouverte car le serveur est arrêté lorsqu'on ferme la fenêtre

  3.b) Lancement de l'application web
	* dans votre exploreur, taper dans la barre d'adresse: "localhost:8000" sur votre pc, et depuis un autre pc du réseau "@IP:8000" où @IP est l'adresse IP (ex: "192.168.0.100") de l'ordinateur où tourne le serveur.


4) Mise à jour de l'applicaiton
	* quitter le serveur
	* sauvegarder au besoin "Source", et séparement la base de données (fichier "db.sqlite3")
	* écraser le répertoire "Source" par le nouveau
	* si besoin de récupérer l'ancienne base de donnée (sous réserve que la structure n'aient pas changé): remplacer "db.sqlite3" par son ancienne version.