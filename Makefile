
manage_py := python app/manage.py

run:
	$(manage_py) runserver

migrate:
	$(manage_py) migrate

makemigrations:
	$(manage_py) makemigrations

createsuperuser:
	$(manage_py) createsuperuser

shell:
	$(manage_py) shell_plus --print-sql

worker:
	cd app && celery -A settings worker -l info -c 4 --pool threads

beat:
	cd app && celery -A settings beat -l info

pytest:
	pytest ./app/tests --cov=app --cov-report html && coverage report --fail-under=79.7754

gunicorn:
	cd app && gunicorn --workers 4 settings.wsgi --max-requests 10000 --log-level info --bind 0.0.0.0:8000
