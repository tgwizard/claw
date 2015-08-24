.PHONY: install test release clean-dist

COVERAGE_SOURCES = claw


install:
	pip install -e .[tests,dev]

test:
	coverage run --source $(COVERAGE_SOURCES) -m py.test tests/
	coverage report -m

release: clean-dist
	python setup.py sdist
	twine upload dist/*

clean-dist:
	rm -rf dist
