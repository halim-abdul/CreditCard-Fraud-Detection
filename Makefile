install:
	pip install -r requirements.txt

test:
	pytest -q

api:
	uvicorn app.main:app --reload

features:
	python scripts/build_features.py data/raw/creditcard.csv data/processed/features.csv
