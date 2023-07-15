release: python manage.py makemigrations --run-syncdb
release: python manage.py migrate --run-syncdb
web: gunicorn pixelpost.wsgi --log-file -
