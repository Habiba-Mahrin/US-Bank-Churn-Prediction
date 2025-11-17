# 📊 **US Bank Churn Prediction**

A machine-learning powered **customer churn prediction web app** built using Flask.  
It analyzes customer details and predicts whether they are likely to leave the bank, helping businesses improve retention.

🔗 **Live Demo:**  
👉 https://us-bank-churn-prediction.onrender.com/

---

## 🏷️ **Badges**

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)  
![Flask](https://img.shields.io/badge/Flask-2-black?logo=flask)  
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Model-green)  
![Render](https://img.shields.io/badge/Hosted%20On-Render-blue?logo=render)  
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 **Project Overview**

This project predicts whether a bank customer will churn using a trained machine-learning model.  
Users enter customer details into a simple web interface, and the model returns **Churn** or **No Churn**.

This application demonstrates:

- End-to-end ML workflow  
- Model deployment using Flask  
- Clean UI for user interaction  
- Hosting on Render with a production-ready setup  

---

## 🧠 **Machine Learning Workflow**

- Load and preprocess dataset  
- Feature encoding and scaling  
- Train ML model (e.g., Random Forest)  
- Save trained model using `pickle`  
- Use the model inside Flask to generate predictions in real-time  

---

## 📁 **Dataset Information**

⚠️ **NOTE:** The Kaggle dataset `bank_churn.csv` is **NOT included** due to licensing and file size.

📥 Download the dataset from Kaggle:  
https://www.kaggle.com/datasets/mathchi/churn-for-bank-customers

After downloading, place it in:


---

## 🛠️ **Tech Stack**

- **Python**
- **Flask**
- **scikit-learn**
- **pandas**
- **numpy**
- **pickle (model storage)**
- **HTML, CSS, Bootstrap**
- **Gunicorn (for deployment)**
- **Render (Hosting)**

---

## 💻 **How to Run Locally**

**1. Clone the repository**
```bash
git clone https://github.com/Habiba-Mahrin/US-Bank-Churn-Prediction.git
cd US-Bank-Churn-Prediction
pip install -r requirements.txt
python app.py

<img width="1861" height="968" alt="Screenshot 2025-11-17 150634" src="https://github.com/user-attachments/assets/d43941cd-3bc5-4286-b05b-2c0dec2898ea" />


