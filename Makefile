export SHELL:=/bin/bash
.ONESHELL:

init:
	virtualenv .venv
	source .venv/bin/activate
	pip install -r requirements.txt
