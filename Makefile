.PHONY: setup setup-python setup-web setup-model train run test fmt clean

# Detect the operating system
ifeq ($(OS),Windows_NT)
    VENV_ACTIVATE = .\venv\Scripts\activate
else
    VENV_ACTIVATE = . venv/bin/activate
endif

setup: setup-python setup-web setup-model
	@echo "✅ Setup complete!"

setup-python:
	@echo "🐍 Setting up Python environment..."
	python -m venv venv
	@echo "📦 Installing Python dependencies..."
	$(VENV_ACTIVATE) && pip install -r requirements.txt -r dev-requirements.txt

setup-web:
	@echo "🌐 Setting up web environment..."
	cd web && npm install --no-audit --no-fund

setup-model:
	@echo "🤖 Downloading model (this may take a while)..."
	$(VENV_ACTIVATE) && python scripts/download_model.py

train:
	@echo "🎯 Training model..."
	$(VENV_ACTIVATE) && python ml/train.py

run:
	@echo "🚀 Starting application..."
	$(VENV_ACTIVATE) && uvicorn api.main:app --reload & cd web && npm run dev

test:
	@echo "🧪 Running tests..."
	$(VENV_ACTIVATE) && pytest -q
	cd web && npm test

fmt:
	@echo "✨ Formatting code..."
	$(VENV_ACTIVATE) && black . && isort .

clean:
	@echo "🧹 Cleaning up..."
	git clean -xfd