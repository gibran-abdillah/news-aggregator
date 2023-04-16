web: gunicorn "newsaggregator.wsgi"
worker: celery -A newsaggregator worker -l info -B
