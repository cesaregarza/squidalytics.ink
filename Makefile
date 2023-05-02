.PHONY: check-deploy

check-deploy:
	@poetry run python squidalytics/manage.py check --deploy

.PHONY: format

format:
	@echo "Running Black..."
	@poetry run black squidalytics
	@echo "Running isort..."
	@poetry run isort squidalytics