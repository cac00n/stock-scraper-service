## ----------------------------------------------------------------------
## Makefile in order to install, format, lint and test code
## ----------------------------------------------------------------------


PRODUCTION_CODE = stock_scraper_service
TESTS = tests

.DEFAULT_GOAL:=all

black = poetry run black $(PRODUCTION_CODE) $(TESTS)
isort = poetry run isort $(PRODUCTION_CODE) $(TESTS)
ruff = poetry run ruff $(PRODUCTION_CODE) $(TESTS)
mypy = poetry run mypy $(PRODUCTION_CODE) $(TESTS)

test = poetry run pytest $(TESTS)

.PHONY: help
help:		## Show this help.
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

.PHONY: install
install:	## Installation of all python packages including dev dependencies
	@echo "Installing packages"
	poetry install
	@echo

.PHONY: format
format:		## Format all python code including tests
	@echo "Formatting imports"
	$(isort)
	@echo "Formatting code"
	$(black)

.PHONY: lint_mypy
lint_mypy: ## Run mypy for type-checking
	@echo "Running mypy type checks"
	$(mypy)
	@echo

.PHONY: lint_ruff
lint_ruff: ## Run ruff to lint code
	@echo "Running linter ruff"
	$(ruff)
	@echo

.PHONY: lint_black
lint_black: ## Run black to lint code
	@echo "Running linter black"
	$(black) --check --diff
	@echo

.PHONY: lint_isort
lint_isort: ## Run isort to check imports
	@echo "Running linter isort"
	$(isort) --check-only
	@echo

.PHONY: lint
lint: lint_black lint_isort lint_ruff lint_mypy		## Lint all python code including tests
	@echo "All linting done."
	@echo

.PHONY: test
test:		## Run all tests in test-folder
	$(test)
	@echo

.PHONY: clean
clean:		## Clean all auxiliary directories
	rm -rf .mypy_cache .pytest_cache .venv .ruff_cache
	@echo

all: install format lint test	## Run stated commands
