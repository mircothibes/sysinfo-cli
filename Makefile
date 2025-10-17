# Makefile for sysinfo-cli project

PYTHON := python
PIP := python -m pip

.PHONY: install dev lint format test run build docker-build docker-run clean

install:
	$(PIP) install --upgrade pip
	$(PIP) install -e .

dev:
	$(PIP) install --upgrade pip
	$(PIP) install -e ".[dev]"

lint:
	ruff check .

format:
	black .

test:
	pytest -q

run:
	$(PYTHON) -m sysinfo.cli

run-json:
	$(PYTHON) -m sysinfo.cli --json

build:
	$(PYTHON) -m pip install build >/dev/null 2>&1 || true
	$(PYTHON) -m build

docker-build:
	docker build -t sysinfo-cli:local .

docker-run:
	docker run --rm sysinfo-cli:local --json

clean:
	rm -rf dist build *.egg-info .pytest_cache .ruff_cache .mypy_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +

