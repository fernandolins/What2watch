# initial:
# 	cp mobdoctor/local_settings.py.example mobdoctor/local_settings.py
# 	setup

clean:
		@find . -name "*.pyc" -delete

deps:
		@pip install -r requirements.txt

test: deps clean
		@python manage.py test --verbosity 2

coverage: deps clean
		@python manage.py test --with-coverage

setup: deps
		@python manage.py syncdb
		@python manage.py migrate

run:
		@python manage.py runserver

help:
		grep '^[^#[:space:]].*:' Makefile | awk -F ":" '{print $$1}'