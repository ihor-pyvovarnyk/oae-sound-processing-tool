all: run

setup:
	pip install -r requirements.txt

run:
	python app

clearPyc:
	find . -type f -name '*.pyc' -delete
