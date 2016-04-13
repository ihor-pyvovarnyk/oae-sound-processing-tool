all: run

install:
	pip install -r requirements.txt

run:
	python app

clear_pyc:
	find . -type f -name '*.pyc' -delete

compile_gui:
	pyuic -o ${PWD}/app/gui/mainwindow.py ${PWD}/resources/gui/mainwindow.ui
