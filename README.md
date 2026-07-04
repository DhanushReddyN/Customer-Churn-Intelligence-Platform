# 📊 Customer Churn Intelligence Platform

An end-to-end Machine Learning application that predicts telecom customer churn using classification algorithms and provides business recommendations through a FastAPI backend and Streamlit dashboard.

---

## 📌 Business Problem

Customer churn is one of the biggest challenges faced by telecom companies.

Acquiring a new customer costs significantly more than retaining an existing one.

This application helps identify customers who are likely to churn so that the business can proactively take retention actions.

---

## ✨ Features

- Customer Churn Prediction
- Business Recommendations
- FastAPI REST API
- Streamlit Dashboard
- Docker Support
- Interactive Analytics
- Bulk Prediction
- Model Comparison

---

## 🏗️ Architecture

```
              Streamlit Dashboard
                     │
                     ▼
                FastAPI Backend
                     │
                     ▼
          Machine Learning Pipeline
                     │
                     ▼
           Churn Prediction Model
```

---

## 📂 Project Structure

```text
customer-churn-intelligence/

├── app/
│   ├── main.py
│   ├── predictor.py
│   ├── schemas.py
│
├── frontend/
│   └── streamlit_app.py
│
├── models/
│   └── churn_model.pkl
│
├── notebooks/
│
├── data/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

Dataset:
Telco Customer Churn Dataset

Source:
IBM Sample Dataset

Rows:
7043

Target Variable:
Churn

---

## 📈 Exploratory Data Analysis

Some important insights discovered:

- Month-to-Month customers churn the most.
- Fiber Optic users have higher churn.
- Customers with short tenure are more likely to churn.
- Tech Support reduces churn.
- Higher monthly charges increase churn probability.

---

## 🤖 Machine Learning Models

Models trained:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

### Model Performance

| Model | Accuracy |
|--------|----------|
| Logistic Regression | 82% |
| Decision Tree | 72% |
| Random Forest | 79% |
| XGBoost | 80% |

Selected Model:

✅ Logistic Regression

Reason:

- Best generalization
- Easy to interpret
- Fast inference
- Suitable for deployment

---

## 🛠 Tech Stack

Python

Pandas

NumPy

Scikit-Learn

FastAPI

Streamlit

Docker

Plotly

Joblib

---

## ⚙ Installation

Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/Customer-Churn-Intelligence-Platform.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run FastAPI

```bash
uvicorn app.main:app --reload
```

Run Streamlit

```bash
streamlit run frontend/streamlit_app.py
```

---

## 🐳 Docker

Build

```bash
docker build -t churn-app .
```

Run

```bash
docker run -p 8000:8000 churn-app
```

Docker Compose

```bash
docker compose up
```

---

## 📷 Screenshots

(Add these later)

Dashboard

Prediction

Swagger

Bulk Prediction

Analytics Dashboard

---

## 🔮 Future Improvements

- SHAP Explainability
- User Authentication
- PostgreSQL Database
- CI/CD Pipeline
- Kubernetes Deployment
- Cloud Monitoring

---

## 👨‍💻 Author

Dhanush Reddy N

GitHub:
https://github.com/DhanushReddyN
