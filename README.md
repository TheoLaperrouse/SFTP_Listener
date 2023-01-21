# Listener de fichiers SFTP

Ce script permet de télécharger automatiquement les fichiers qui arrivent sur un serveur SFTP. Il vérifie toutes les 5 minutes s'il y a de nouveaux fichiers sur le serveur, et si c'est le cas, il les télécharge sur la racine du projet.

## Prérequis

- Python 3.7 ou supérieur
- bibliothèque `paramiko` pour la connexion SFTP
- bibliothèque `dotenv` pour la gestion des informations de connexion
- Un serveur SFTP accessible avec les informations de connexion dans un fichier .env

## Installation

1. Installez les dépendances en utilisant pip : `pip install -r requirements.txt`
2. Remplir le fichier .env avec les informations de connexion
3. Exécutez le script : `python sftp_download.py`

## Déploiement en utilisant Docker-Compose

1. Remplir le fichier .env avec les informations de connexion
2. Exécutez la commande `docker-compose up -d` dans le répertoire où se trouve le fichier docker-compose.yml

## Test

Vous pouvez utiliser le fichier `test_sftp_download.py` pour vérifier que le script fonctionne correctement. Assurez-vous que le serveur SFTP de test est configuré avec les informations de connexion stockées dans le fichier .env avant les tests.

## Utilisation

Une fois le script lancé, il va continuer à vérifier toutes les 5 minutes (par défaut) s'il y a de nouveaux fichiers sur le serveur SFTP et les télécharger automatiquement à la racine du projet.

## Remarques

- Le script utilise les informations de connexion SFTP stockées dans le fichier .env. Assurez-vous de les remplir avant de lancer le script ou de déployer le conteneur.
- Le port SFTP par défaut est 2222, vous pouvez le changer en modifiant le fichier docker-compose.yml si nécessaire.
- Le volume associé est défini à la racine du projet, les fichiers téléchargés seront stockés à la racine du projet. Vous pouvez changer le chemin pour stocker les fichiers dans un autre emplacement.
