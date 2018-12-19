<<<<<<< HEAD
web: daphne hellod5world.asgi:application --port $port --bind 0.0.0.0
worker: python manage.py runworker channels -v2
=======
web: gunicorn helloworld.wsgi
web: daphne helloworld.asgi:application --port $port --bind 0.0.0.0
worker: python manage.py runworker channels -v2
>>>>>>> 44e95f6776cffdb2b004a9832151f3b8234bff17
