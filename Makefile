# All process that able to be run by make.
.PHONY: dev pre-commit lint lint-s black mypy flake8 pylint pip-check-reqs toml-sort test release clean deepclean docs devdocs

# Set package dir
PKGDIR := my_repo

# Prepare dev environments:
# If not in CICD mode, set pre-commit
# Install all dependencies
dev:
	-[ "${CI}" != "true" ] && pre-commit install --hook-type pre-commit
	pip install --user --requirement ./requirements/develop.txt

##Run pre-commit for all files.
pre-commit:
	pre-commit run --all-files

# [Experimental] Check missing/redundant requirements.
pip-check-reqs:
	pip-missing-reqs ${PKGDIR}
	pip-extra-reqs ${PKGDIR}

# Trigger tests.
test:
	set -x
	python -m pytest -x -s -v --cov=${PKGDIR} --cov-fail-under=$(or $(TEST_COVERAGE_THRESHOLD),0) .

# Release package, include build and publish.
release:
	python3 setup.py sdist bdist_wheel --universal
	twine upload dist/*

# Remove common intermediate files.
clean:
	find . -name '*.pyc' -print0 | xargs -0 rm -f
	find . -name '*.swp' -print0 | xargs -0 rm -f
	find . -name '.DS_Store' -print0 | xargs -0 rm -rf
	find . -name '__pycache__' -print0 | xargs -0 rm -rf
	-rm -rf \
		*.egg-info \
		.coverage \
		.eggs \
		.mypy_cache \
		.pytest_cache \
		Pipfile* \
		build \
		dist \
		output \
		public

# Remove common intermediate files alongside with `pre-commit` hook.
deepclean: clean
	pre-commit uninstall --hook-type pre-push
