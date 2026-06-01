import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score, mean_absolute_error

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

df = pd.read_excel(
    "data/Case_Study_1_Data.xlsx"
)

# Feature Engineering

df["Date Sold"] = pd.to_datetime(
    df["Date Sold"]
)

df["Sale_Year"] = df["Date Sold"].dt.year

df["Sale_Month"] = df["Date Sold"].dt.month

df["Property_Age"] = (
    df["Sale_Year"]
    - df["Year Built"]
)

# Remove IDs

df.drop(
    ["Property ID", "Date Sold"],
    axis=1,
    inplace=True
)

# Encoding

for col in df.select_dtypes(
    include="object"
).columns:

    le = LabelEncoder()

    df[col] = le.fit_transform(
        df[col].astype(str)
    )

# Features

X = df.drop("Price", axis=1)

y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

models = {
    "LinearRegression": LinearRegression(),

    "RandomForest": RandomForestRegressor(
        n_estimators=200,
        n_jobs=-1,
        random_state=42
    ),

    "XGBoost": XGBRegressor(
        n_estimators=500,
        max_depth=8,
        learning_rate=0.05,
        n_jobs=-1,
        random_state=42
    )
}

best_model = None
best_score = 0

for name, model in models.items():

    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    score = r2_score(
        y_test,
        pred
    )

    print(
        f"{name} R2: {score}"
    )

    if score > best_score:

        best_score = score

        best_model = model

joblib.dump(
    best_model,
    "model/house_price_model.pkl"
)

print(
    "Model Saved Successfully"
)
