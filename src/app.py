from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI(
    title="House Price Prediction API"
)

model = joblib.load(
    "model/house_price_model.pkl"
)

@app.get("/")
def root():

    return {
        "message":
        "API Running"
    }

@app.post("/predict")
def predict(data: dict):

    df = pd.DataFrame(
        [data]
    )

    prediction = model.predict(
        df
    )

    return {
        "predicted_price":
        float(prediction[0])
    }
