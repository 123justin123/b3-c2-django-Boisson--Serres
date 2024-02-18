# b3-c2-django-Boisson--Serres

Installez les dépendances en exécutant :

```bash
pip install -r requirements.txt
```

## Configuration de la base de données

Ce projet utilise SQLite comme système de gestion de base de données, qui est le système par défaut de Django. Aucune configuration supplémentaire n'est nécessaire.

## Migrations

Exécutez les migrations pour initialiser votre base de données :

```bash
python manage.py makemigrations PasswordManager
python manage.py migrate
```

## Démarrer le serveur de développement

Lancez le serveur de développement Django :

```bash
python manage.py runserver
```

Accédez à `http://127.0.0.1:8000/` dans votre navigateur pour voir le projet en action.
