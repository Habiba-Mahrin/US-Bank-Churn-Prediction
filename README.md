# Churn Prediction Full App (minimal)

## What's included
- `src/` : preprocessing, training, and model utils
- `app/` : FastAPI server and simple HTML UI
- `requirements.txt`, `Dockerfile`, `Procfile`

**NOTE:** The Kaggle dataset `bank_churn.csv` is NOT included due to licensing & size.
Download from: https://www.kaggle.com/datasets/mathchi/churn-for-bank-customers
Place the CSV at `data/bank_churn.csv`

## Quick start (local)
1. Create a Python venv and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # mac/linux
   venv\Scripts\activate    # windows
   ```
2. Install requirements:
   ```
   pip install -r requirements.txt
   ```
3. Put `bank_churn.csv` into the `data/` folder.
4. Train model (this will create `models/best_model.joblib`):
   ```
   python src/train.py
   ```
5. Run the app:
   ```
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```
6. Open http://localhost:8000 in your browser.

## Replit / Deployment notes
- On Replit upload the repo files and the CSV (or fetch it at runtime).
- Set the run command to:
  `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

## LLM integration
- This repo contains placeholders for LLM calls. Add your provider calls in `app/main.py`.
