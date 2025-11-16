from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pandas as pd
from pathlib import Path
import os
from src.model_utils import load_model

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / 'models' / 'best_model.joblib'

app = FastAPI()
app.mount('/static', StaticFiles(directory=str(ROOT / 'app' / 'static')), name='static')
templates = Jinja2Templates(directory=str(ROOT / 'app' / 'templates'))

model = None
try:
    model = load_model(MODEL_PATH)
except Exception as e:
    print('Model not loaded (train first):', e)

@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.post('/predict')
async def predict(request: Request):
    payload = await request.json()
    df = pd.DataFrame([payload])
    if model is None:
        return JSONResponse({'error': 'model not found - run python src/train.py first'}, status_code=400)
    prob = model.predict_proba(df)[:, 1][0]
    pred = int(prob > 0.5)
    return JSONResponse({'churn_prob': float(prob), 'churn_pred': pred})

@app.post('/explain_and_email')
async def explain_and_email(request: Request):
    payload = await request.json()
    prob = payload.get('churn_prob', None)
    if prob is None:
        df = pd.DataFrame([payload])
        if model is None:
            return JSONResponse({'error': 'model not found - run python src/train.py first'}, status_code=400)
        prob = float(model.predict_proba(df)[:,1][0])
    prob = float(prob)
    explanation = []
    if prob > 0.7:
        explanation.append('High churn risk — customer shows multiple risk signals.')
    elif prob > 0.4:
        explanation.append('Moderate churn risk — monitor and try retention offers.')
    else:
        explanation.append('Low churn risk — normal usage.')
    name = payload.get('Name', 'Customer')
    email = f"Subject: We value you, {name}!\n\nHi {name},\n\nWe noticed you might be considering other options. Based on your account, we can offer a personalized plan to help you get more value. Reply here or click to book a short call with our support team.\n\nBest,\nYour Bank"
    return JSONResponse({'explanation': explanation, 'email': email})
