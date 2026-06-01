import joblib
import pandas as pd

model = joblib.load(
    "model/house_price_model.pkl"
)

sample = pd.DataFrame([
    {
        "Location":1,
        "Size":2500,
        "Bedrooms":3,
        "Bathrooms":2,
        "Year Built":2015,
        "Condition":1,
        "Type":1,
        "Sale_Year":2025,
        "Sale_Month":5,
        "Property_Age":10
    }
])

prediction = model.predict(
    sample
)

print(
    prediction
)
