import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE

NUM_FEATURES = ['CreditScore', 'Age', 'Balance', 'EstimatedSalary', 'Tenure', 'NumOfProducts']
CAT_FEATURES = ['Geography', 'Gender', 'HasCrCard', 'IsActiveMember']
TARGET = 'Exited'

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def build_preprocessor(num_features=NUM_FEATURES, cat_features=CAT_FEATURES):
    num_pipe = Pipeline([('scale', StandardScaler())])
    cat_pipe = Pipeline([('ohe', OneHotEncoder(handle_unknown='ignore', sparse=False))])
    preproc = ColumnTransformer([
        ('num', num_pipe, num_features),
        ('cat', cat_pipe, cat_features)
    ])
    return preproc

def prepare_train_test(df: pd.DataFrame, test_size=0.2, random_state=42, smote=False):
    X = df[NUM_FEATURES + CAT_FEATURES]
    y = df[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=test_size, random_state=random_state)

    if smote:
        sm = SMOTE(random_state=random_state)
        X_train_enc = pd.get_dummies(X_train, columns=CAT_FEATURES, drop_first=False)
        X_train_res, y_train_res = sm.fit_resample(X_train_enc, y_train)
        X_test_enc = pd.get_dummies(X_test, columns=CAT_FEATURES, drop_first=False)
        X_test_enc = X_test_enc.reindex(columns=X_train_res.columns, fill_value=0)
        return X_train_res, X_test_enc, y_train_res, y_test

    return X_train, X_test, y_train, y_test
