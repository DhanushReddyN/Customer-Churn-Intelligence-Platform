import joblib
import pandas as pd
from datetime import datetime
import os

# Load the model
model = joblib.load("models/churn_model.pkl")


def predict_churn(customer):

    input_df = pd.DataFrame([customer])

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_data = {
        "Timestamp": timestamp,
        "Prediction": "Churn" if prediction == 1 else "No Churn",
        "Probability": round(float(probability * 100), 2)
    }

    os.makedirs("logs", exist_ok=True)

    log_file = "logs/predictions.csv"

    log_df = pd.DataFrame([log_data])

    if os.path.exists(log_file):
        log_df.to_csv(
            log_file,
            mode="a",
            header=False,
            index=False
        )
    else:
        log_df.to_csv(
            log_file,
            index=False
        )

    return prediction, probability