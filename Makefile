.PHONY: install test release clean-dist

install:
	pip install -e .[tests,dev]

test:
	nosetests

release: clean-dist
	python setup.py sdist
	twine upload dist/*

clean-dist:
	rm -rf dist
