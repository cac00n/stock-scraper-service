PRODUCTION_CODE = stock_scraper_service
TESTS = tests

all: install format lint test

install:
	@echo "Installing packages"
	poetry install

format:
	@echo "Formatting imports"
	poetry run isort $(PRODUCTION_CODE) $(TESTS)
	@echo "Formatting code"
	poetry run black $(PRODUCTION_CODE) $(TESTS)

lint:
	@echo "Linting code"
	poetry run ruff $(PRODUCTION_CODE) $(TESTS)
	@echo "Running mypy type checks"
	poetry run mypy $(PRODUCTION_CODE) $(TESTS)

test:
	poetry run pytest $(TESTS)

clean:
	rm -rf .mypy_cache .pytest_cache .venv .ruff_cache