.PHONY: help install install-dev test test-cov lint format clean build publish docs

help: ## Show this help message
	@echo "DevOpsForge - Professional DevOps Automation Tool"
	@echo ""
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Install the package
	pip install -e .

install-dev: ## Install development dependencies
	pip install -r requirements.txt
	pip install -e .

test: ## Run tests
	python -m pytest

test-cov: ## Run tests with coverage
	python -m pytest --cov=devopsforge --cov-report=html --cov-report=term

lint: ## Run linting checks
	flake8 devopsforge/
	black --check devopsforge/
	isort --check-only devopsforge/

format: ## Format code
	black devopsforge/
	isort devopsforge/

clean: ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: ## Build package
	python setup.py sdist bdist_wheel

publish: ## Publish to PyPI (requires twine)
	twine upload dist/*

docs: ## Generate documentation
	# Add documentation generation commands here
	@echo "Documentation generation not yet implemented"

check: ## Run all checks (lint, test, format)
	@echo "Running all checks..."
	@make lint
	@make test
	@make format

pre-commit: ## Run pre-commit checks
	@echo "Running pre-commit checks..."
	@make format
	@make lint
	@make test

demo: ## Run the demo script
	python demo.py

sample-test: ## Test with sample project
	devopsforge analyze sample_python_project
	devopsforge generate sample_python_project -o ./output
	devopsforge suggest sample_python_project

version: ## Show current version
	@python -c "import devopsforge; print(devopsforge.__version__)"

requirements: ## Update requirements.txt
	pip freeze > requirements.txt

venv: ## Create virtual environment
	python -m venv venv
	@echo "Virtual environment created. Activate with:"
	@echo "  source venv/bin/activate  # On Unix/macOS"
	@echo "  venv\\Scripts\\activate     # On Windows"

setup: ## Complete development setup
	@echo "Setting up development environment..."
	@make venv
	@echo "Please activate your virtual environment and run:"
	@echo "  make install-dev"

.PHONY: help install install-dev test test-cov lint format clean build publish docs check pre-commit demo sample-test version requirements venv setup
