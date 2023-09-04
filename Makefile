install:
		poetry install
dev:
		poetry run flask --app page_analyzer:app run
PORT ?= 8000
start:
		poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app
test-cov:
		poetry run pytest --cov=page_analyzer
test-coverage:
		poetry run pytest --cov-report xml --cov=page_analyzer
lint:
		poetry run flake8 page_analyzer
