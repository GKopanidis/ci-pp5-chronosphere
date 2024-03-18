release: python manage.py makemigrations && python manage.py migrate
web: gunicorn chronosphere_drf_api.wsgi
web: serve -s build