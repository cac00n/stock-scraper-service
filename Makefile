## ----------------------------------------------------------------------
## Makefile in order to install, format, lint and test code
## ----------------------------------------------------------------------


PRODUCTION_CODE = stock_scraper_service
TESTS = tests


help:		## Show this help.
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

install:	## Installation of all python packages including dev dependencies
	@echo "Installing packages"
	poetry install

format:		## Format all python code including tests
	@echo "Formatting imports"
	poetry run isort $(PRODUCTION_CODE) $(TESTS)
	@echo "Formatting code"
	poetry run black $(PRODUCTION_CODE) $(TESTS)

lint:		## Lint all python code including tests
	@echo "Linting code"
	poetry run ruff $(PRODUCTION_CODE) $(TESTS)
	@echo "Running mypy type checks"
	poetry run mypy $(PRODUCTION_CODE) $(TESTS)

test:		## Run all tests in test-folder
	poetry run pytest $(TESTS)

clean:		## Clean all auxiliary directories
	rm -rf .mypy_cache .pytest_cache .venv .ruff_cache

all: install format lint test	## Run stated commands
