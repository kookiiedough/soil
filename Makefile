.PHONY: setup train run test fmt clean

setup:
	python -m venv venv
	. venv/bin/activate && pip install -r requirements.txt -r dev-requirements.txt
	cd web && npm install
	. venv/bin/activate && python scripts/download_model.py

train:
	. venv/bin/activate && python ml/train.py

run:
	. venv/bin/activate && uvicorn api.main:app --reload & cd web && npm run dev

test:
	. venv/bin/activate && pytest -q
	cd web && npm test

fmt:
	. venv/bin/activate && black . && isort .

clean:
	git clean -xfd