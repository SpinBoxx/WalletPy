![logo WalletPY](./WalletPy/static/logo.ico)

# WalletPy

WalletPy est un site permettant de consulter les données en temps réel de différentes cryptoactif comme le bitcoin. Il permet aussi de pouvoir y lié son portefeuille metamask pour pouvoir consulter les informations de transactions ou des soldes.

## Demo

L'application est disponible à cette URL : https://walletpy.cleverapps.io/

## Administration

Compte par defaut admin :
- admin@admin.fr
- admin
- URL : https://walletpy.cleverapps.io/admin

### Coin

Les coins sont les données de cryptomonnaies que le site récupère pour afficher les différentes informations sur le dashboard

**Champs :**
- symbol : BTC, ETH
- name: bitcoin, ethereum

### Fiat

Les fiat sont les monnaies fiduciaires disponible pour la conversion (Exemple Bitcoin => Dollar)

**Champs :**
- symbol : $, €...
- short_name: usd, eur
- name: american dollar, euro...

## Installation

### Pour lancer le projet via docker-compose.

La branche `feature/mariadb_docker_integration` possède un Dockerfile et un docker-compose.yml, c'est la seule branche disponible pour utiliser docker (pas merge dans main)

Se positionner dans le dossier parent du projet et lancer la commande : <br />
`docker-compose up`  <br />
Docker va build les containers, un `db` pour la base de données MySQL et un `web` pour le projet python Django. <br />
Ensuite se rendre sur http://localhost:8080 <br />

**un superuser par defaut est disponible voir la section Administration**

### Pour utiliser en local

La branche `main` utilise SQLite <br />
Requis :  <br />
python et pip d'installés  <br />
Lancer un `pip install -r requirement.txt`  <br />
Puis `python manage.py migrate` pour mettre à jour les models dans la base  <br />
Enfin `python manage.py runserver 8080`  <br />
Ensuite se rendre sur http://localhost:8080  <br />

**Pas de superuser par defaut**
Pour en créer lancer `python manage.py createsuperuser` et suivre les instructions

## Test

 - ### Pour pouvoir executer des tests il faut se rendre dans Walletpy/walletpy

 - ### Des tests sont disponibles dans le fichier (et executable avec la commande) :
    - custom_auth ( python ./manage.py test custom_auth )
