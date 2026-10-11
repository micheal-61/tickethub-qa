.PHONY: install test clean

install:
	pip install -r requirements.txt

test:
	pytest tests/ -v --junitxml=ci/test-results.xml

clean:
	rm -rf .pytest_cache ci/test-results.xml
