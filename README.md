# TP Framework - Licence Pro Prism

Ce dépôt contient tous mes TP réalisés dans le cadre de ma licence professionnelle Prism en développement Framework en
Django.

## Description

Dans ce dépôt, vous trouverez le TP que j'ai réalisés tout au long de ma formation.

## Comment utiliser ce dépôt

Ce dépôt peut être utilisé comme référence pour les projets futurs ou pour aider les autres étudiants en difficulté. Il
est à noter que les TP présentés dans ce dépôt ont été réalisés dans le cadre de ma formation, il est donc conseillé de
respecter les droits d'auteur et de ne pas les réutiliser tels quels.

Si vous avez des questions sur l'utilisation de ce dépôt, n'hésitez pas à me contacter.

# Comment installer le projet

Pour installer le projet, il faut suivre les étapes suivantes :

## Cloner le projet

``` bash
git clone https://github.com/Fredray-21/LP-Prism-Django.git
```

## Créer un environnement virtuel

``` bash
python -m venv env
```

## Activer l'environnement virtuel
### Windows
``` bash
env\Scripts\activate
```

### Linux
``` bash
source env/bin/activate
```

## Installer les dépendances

``` bash
pip install -r requirements.txt
```

## Créer la base de données

``` bash
python manage.py makemigrations
python manage.py migrate
```

## Si besoin : Créer un super utilisateur

``` bash
python manage.py createsuperuser
```

## Lancer le serveur

``` bash
python manage.py runserver
```

# Notes sur le projet

### Un jeu de données est fourni avec le projet.

<table>
<tr>
<td>Utilisateur</td>
<td>Password</td>
</tr>
<tr>
<td>admin</td>
<td>Administrateur21</td>
</tr>
<tr>
<td>test</td>
<td>PasswordTest21</td>
</tr>
</table>
