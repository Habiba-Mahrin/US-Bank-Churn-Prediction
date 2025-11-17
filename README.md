📊 US Bank Churn Prediction

A machine-learning powered web application built with Flask, designed to predict whether a bank customer is likely to churn.
✔ Live demo hosted on Render
✔ Uses a trained ML model (Random Forest / Logistic Regression — depending on your project)
✔ Clean UI + fully container-ready structure

🚀 Live Demo

👉 https://us-bank-churn-prediction.onrender.com/

🏷️ Badges










📌 Project Overview

Bank churn prediction helps financial institutions identify customers who are likely to leave the bank.
This project provides:

A trained machine learning model

A Flask web interface

Real-time predictions based on customer inputs

Clean architecture & deployable structure

The core idea is to help banks understand churn behavior to improve retention.

🧠 Machine Learning Workflow

Load and clean dataset

Perform feature engineering

Train ML model (Random Forest / Logistic Regression)

Save trained model using pickle

Use model inside Flask app for predictions

🧱 Architecture Diagram
User Input → Flask UI → Preprocessing → ML Model → Prediction → Output (Churn / No Churn)


(If you want, I can generate a real image diagram too.)

📥 Dataset

NOTE:
The Kaggle dataset bank_churn.csv is NOT included in this repository due to licensing restrictions and file size.

🔗 Download the dataset from Kaggle:
https://www.kaggle.com/datasets/mathchi/churn-for-bank-customers

After downloading, place the file here:

data/bank_churn.csv

🛠️ Tech Stack
Component	Technology
Backend	Flask (Python)
Machine Learning	scikit-learn, pandas, numpy
UI	HTML, CSS, Bootstrap
Hosting	Render
Model Storage	Pickle (.pkl file)
📂 Project Structure
churn_app/
│── app/
│   ├── static/
│   ├── templates/
│   ├── model.pkl
│   ├── __init__.py
│   ├── routes.py
│── data/
│   ├── bank_churn.csv  (NOT included — download from Kaggle)
│── app.py
│── requirements.txt
│── README.md
│── Procfile (for Render)

🏃 How to Run Locally

1️⃣ Clone repository

git clone https://github.com/Habiba-Mahrin/US-Bank-Churn-Prediction.git
cd US-Bank-Churn-Prediction


2️⃣ Install dependencies

pip install -r requirements.txt


3️⃣ Run Flask app

python app.py


4️⃣ Visit in browser

http://127.0.0.1:5000

🌐 Deployment (Render)

Render automatically detects your Flask app using:

app.py

requirements.txt

Procfile

Example Procfile:

web: gunicorn app:app

🖼️ Screenshots

(Add your app screenshot here)

📜 License

This project is licensed under the MIT License.

⭐ Support

If this project helped you, please ⭐ star the repo!
