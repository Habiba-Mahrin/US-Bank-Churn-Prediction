import os
from pathlib import Path
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score

from src.data_prep import load_data, build_preprocessor, prepare_train_test
from src.model_utils import save_model

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / 'data' / 'bank_churn.csv'
MODEL_DIR = ROOT / 'models'
MODEL_DIR.mkdir(parents=True, exist_ok=True)

def main():
    print('Loading data...')
    df = load_data(DATA_PATH)

    print('Preparing data...')
    X_train, X_test, y_train, y_test = prepare_train_test(df)
    preproc = build_preprocessor()

    models = {
        'logreg': (LogisticRegression(max_iter=2000), {'clf__C': [0.01, 0.1, 1, 10]}),
        'knn': (KNeighborsClassifier(), {'clf__n_neighbors': [3, 5, 7]}),
        'dt': (DecisionTreeClassifier(random_state=42), {'clf__max_depth': [3, 5, 8]}),
        'rf': (RandomForestClassifier(random_state=42), {'clf__n_estimators': [50, 100], 'clf__max_depth': [5, 10]}),
        'xgb': (XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42), {'clf__n_estimators': [50, 100], 'clf__max_depth': [3, 6]})
    }

    best_score = 0.0
    best_name = None
    best_model = None

    for name, (clf, params) in models.items():
        print(f'Training {name}...')
        pipe = Pipeline([('pre', preproc), ('clf', clf)])
        gs = GridSearchCV(pipe, param_grid=params, cv=3, scoring='roc_auc', n_jobs=-1)
        gs.fit(X_train, y_train)
        score = roc_auc_score(y_test, gs.predict_proba(X_test)[:, 1])
        print(f'  {name} ROC AUC on test: {score:.4f} best_params: {gs.best_params_}')
        if score > best_score:
            best_score = score
            best_name = name
            best_model = gs.best_estimator_

    print(f'Best model: {best_name} with ROC AUC {best_score:.4f}')
    save_path = MODEL_DIR / 'best_model.joblib'
    save_model(best_model, save_path)
    print('Saved best model to', save_path)

if __name__ == '__main__':
    main()
