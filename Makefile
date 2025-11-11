.PHONY: install test run docker get-data scrape clean train all run-api run-streamlit

install:
	python -m venv .venv
	.venv\Scripts\activate
	pip install -r requirements.txt

test:
	pytest -q

run-api:
	uvicorn src.api:app --reload --port 8000

run-streamlit:
	streamlit run src/app.py

docker:
	docker build -t my_project .

get-data:
	python src/fetch_data.py

scrape:
	python src/scrape_books.py

clean:
	python src/clean_books.py

train:
	python src/classify.py

all: get-data scrape clean train
