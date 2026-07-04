from fastapi import FastAPI

from app.schemas import Customer
from app.predictor import predict_churn

app = FastAPI(title="Customer Churn Prediction API")


@app.get("/")
def home():
    return {"message": "API Running"}

@app.post("/predict")
def predict(customer: Customer):

    prediction, probability = predict_churn(customer.dict())
    prediction, probability = predict_churn(
        customer.model_dump()
    )

    return {
    "prediction": "Churn" if prediction == 1 else "No Churn",
    "probability": round(float(probability * 100), 2)
}