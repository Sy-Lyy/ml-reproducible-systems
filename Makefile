.PHONY: install test run docker

install:
	python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

test:
	pytest -q

run:
	python -m src

docker:
	docker build -t my_project .

get-data:
	python fetch_data.py

scrape:
	python scrape_books.py

clean:
	python clean_books.py   # optional cleaning step

train:
	python classify.py

all: get-data scrape train