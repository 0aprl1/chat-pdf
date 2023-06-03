ENV_NAME:= venv
DB_NAME:= test-vector-db
PDF_NAME:= sample-document

env:
	python3 -m venv $(ENV_NAME) && source $(ENV_NAME)/bin/activate

set-up-env: env
	pip3 install -r requirements.txt

index-pdf-document: set-up-env
	DB_NAME=$(DB_NAME) PDF_NAME=$(PDF_NAME) && python3 scripts/index.py

chat: set-up-env
	DB_NAME=$(DB_NAME) && python3 scripts/chat.py

demo: set-up-env index-pdf-document chat