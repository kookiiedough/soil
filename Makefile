.PHONY: setup setup-python setup-web setup-model train run test fmt clean

setup: setup-python setup-web setup-model
	@echo "✅ Setup complete!"

setup-python:
	@echo "🐍 Setting up Python environment..."
	python -m venv venv
	.\venv\Scripts\activate && pip install -r requirements.txt -r dev-requirements.txt

setup-web:
	@echo "🌐 Setting up web environment..."
	cd web && npm install --no-audit --no-fund

setup-model:
	@echo "🤖 Downloading model (this may take a while)..."
	.\venv\Scripts\activate && python scripts/download_model.py

train:
	@echo "🎯 Training model..."
	.\venv\Scripts\activate && python ml/train.py

run:
	@echo "🚀 Starting application..."
	.\venv\Scripts\activate && uvicorn api.main:app --reload & cd web && npm run dev

test:
	@echo "🧪 Running tests..."
	.\venv\Scripts\activate && pytest -q
	cd web && npm test

fmt:
	@echo "✨ Formatting code..."
	.\venv\Scripts\activate && black . && isort .

clean:
	@echo "🧹 Cleaning up..."
	git clean -xfd