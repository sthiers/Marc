	DEPLOIEMENT LOCAL DE L'APPLICATION PERSISTENT
	Mars 2015

Note: le vrai d�ploiement n�cessite un v�ritable serveur ( linux + nginx (reverse proxy) + uwsgi (serveur applicatif) )

1) Installation des d�pendances sous Windows (version 7):

  1.a) installation de PYTHON (version 3.4.3) :
	* installer l'application: https://www.python.org/downloads/release/python-343/
		note: laisser les options par d�faut (il faut que les packages "pip" et "setuptools" soient install�s).
	* configuration des variables d'environnement:
	- menu D�marrer, rechercher:"variables d'environnement"
	- dans la fen�tre qui s'ouvre ("propri�t�s syst�mes") et dans l'onglet ("avanc�"), cliquer sur "Variables d'environnnement"
	- dans la liste d�filante inf�rieure, s�lectionner la variable "Path", puis cliquer sur "Editer".
	- rajouter � la fin de la liste la cha�ne suivante: ";C:\Python34;C:\Python43\Scripts", o� "Python34" correspond au dossier o� Python 3 a �t� install�
	- cliquer "Ok" puis "Appliquer".
	* v�rification de l'installation: 
	- ouvrir un shell de commande (raccourci clavier: "touche windows+R", puis taper "cmd" et "Ok": 
	- ex�cuter dans le shell "python": une nouvelle invite (">>>") doit appara�tre, o� on peut ex�cuter du code python 
		(taper "quit()" ou "exit()" pour revenir au shell). (note: un raccourci pour stopper un processus dans le shell : "ctrl+c" )


  1.b) installation de DJANGO (version 1.7.7) : 
	- ouvrir un shell de commande, puis ex�cuter "pip install django==1.7.7"


2) Installation du projet:
	* copier le dossier "Source" dans le r�pertoire de votre choix (attention: ne rien y modifier!), si possible dans votre dossier d'utilisateur windows pour ne pas avoir � trop naviger dans le shell (plusieurs "cd")
	* v�rification de l'installation: dans un shell, ex�cuter "python", puis dans le shell python qui s'affiche, ex�cuter successivement "import django", touche Entr�e, puis "django.VERSION": la version de django devrait s'afficher.


3) Lancement de l'application:

  3.a) Lancement du serveur int�gr� � DJANGO (en �coute sur le port r�seau 8000 )
	* lancer un shell, puis naviger (cd "nom du r�pertoire", ou 'cd .." pour revenir en arri�re) jusqu'au r�pertoire "Source"
	* ex�cuter la commande "manage.py runserver"
	* IMPORTANT: laisser la fen�tre ouverte car le serveur est arr�t� lorsqu'on ferme la fen�tre

  3.b) Lancement de l'application web
	* dans votre exploreur, taper dans la barre d'adresse: "localhost:8000" sur votre pc, et depuis un autre pc du r�seau "@IP:8000" o� @IP est l'adresse IP (ex: "192.168.0.100") de l'ordinateur o� tourne le serveur.


4) Mise � jour de l'applicaiton
	* quitter le serveur
	* sauvegarder au besoin "Source", et s�parement la base de donn�es (fichier "db.sqlite3")
	* �craser le r�pertoire "Source" par le nouveau
	* si besoin de r�cup�rer l'ancienne base de donn�e (sous r�serve que la structure n'aient pas chang�): remplacer "db.sqlite3" par son ancienne version.