`![logo WalletPY](WalletPy/static/logo.ico)`

# WalletPy

WalletPy est un site permettant de consulter les données en temps réel de différentes cryptoactif comme le bitcoin. Il permet aussi de pouvoir y lié son portefeuille metamask pour pouvoir consulter les informations de transactions ou des soldes.

## Demo

L'application est disponible à cette URL : https://walletpy.cleverapps.io/

## Administration

Compte par defaut admin :
admin@admin.fr
admin
URL : https://walletpy.cleverapps.io/admin

### Coin

Les coins sont les données de cryptomonnaies que le site récupère pour afficher les différentes informations sur le dashboard

**Champs :**
Symbol : BTC, ETH
name: bitcoin, ethereum

### Fiat

Les fiat sont les monnaies fiduciaires disponible pour la conversion (Exemple Bitcoin => Dollar)

**Champs :**
Symbol : $, €...
short_name: usd, eur
name: american dollar, euro...

## Installation

### Pour lancer le projet via docker-compose.

La branche `feature/mariadb_docker_integration/WalletPy` possède un Dockerfile et un docker-compose.yml, c'est la seule branche disponible pour utiliser docker (pas merge dans main)

Se positionner dans le dossier parent du projet et lancer la commande :
`docker-compose up`
Docker va build les containers, un `db` pour la base de données MySQL et un `web` pour le projet python Django.
Ensuite se rendre sur http://localhost:8080

**un superuser par defaut est disponible voir la section Administration**

### Pour utiliser en local

La branche `main` utilise SQLite
Requis :
python et pip d'installés
Lancer un `pip install -r requirement.txt`
Puis `python manage.py migrate` pour mettre à jour les models dans la base
Enfin `python manage.py runserver 8080`
Ensuite se rendre sur http://localhost:8080

**Pas de superuser par defaut**
Pour en créer lancer `python manage.py createsuperuser` et suivre les instructions
