.PHONY: install test release post-dep-install clean-dist

COVERAGE_SOURCES = claw


install:
	pip install -e .[tests,dev]

test:
	coverage run --source $(COVERAGE_SOURCES) -m py.test tests/
	coverage report -m

release: clean-dist
	python setup.py sdist
	twine upload dist/*

post-dep-install:
	@echo "Dependencies installed successfully"

clean-dist:
	rm -rf dist
