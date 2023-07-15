web: python manage.py makemigrations --run-syncdb
web: python manage.py migrate --run-syncdb
web: gunicorn pixelpost.wsgi --log-file -
