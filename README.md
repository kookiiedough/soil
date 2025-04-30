# Biodynamic Offline

A soil health prediction system that works entirely offline, analyzing FASTQ files to provide actionable farming recommendations.

## Features

- 🧬 Analyze FASTQ genomic data files for soil microbiome assessment
- 📊 Predict soil health metrics using machine learning
- 💬 Get personalized farming recommendations via LLM-powered chat
- 🔌 Works 100% offline - no internet or cloud services required

## Screenshots

![Dashboard](./screenshots/dashboard.png)
![Results](./screenshots/results.png)

## Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/biodynamic-offline.git
cd biodynamic-offline

# Set up the environment and install dependencies
make setup

# Train the model (optional - pre-trained model included)
make train

# Run the application
make run
```

Then open your browser to:
- Frontend: http://localhost:5173
- API docs: http://localhost:8000/docs

## System Requirements

- GitHub Codespace (Ubuntu 22.04)
- 4 vCPU, 8 GB RAM
- No Docker or cloud services needed

## Project Structure

```
/api             - FastAPI backend (upload, predict, chat)
/ml              - feature_engineer.py, train.py, soil_xgb.pkl
/llm             - rag.py (llama-cpp-python)
/web             - Vite + React + Tailwind dashboard
/data            - sample.fastq, dummy_soil.csv
/tests           - PyTest + Vitest specs
/scripts         - helper shell scripts
requirements.txt - runtime deps
dev-requirements.txt - lint & test deps
Makefile         - setup · train · run · test · fmt · clean
```

## Development

```bash
# Run tests
make test

# Format code
make fmt

# Clean project
make clean
```

## License

MIT