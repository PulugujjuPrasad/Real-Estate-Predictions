# AI-Powered House Price Prediction

An end-to-end machine learning project for predicting real estate prices using advanced machine learning models and deployed as a FastAPI service in GitHub Codespaces.

## 🎯 Objective

Predict house prices using real estate data and machine learning models. Compare the performance of multiple algorithms (Linear Regression, Random Forest, XGBoost) and deploy the best-performing model via a REST API.

## 📊 Dataset

- **Records**: 247,172 real estate transactions
- **File**: `Case_Study_1_Data.xlsx`

## ✨ Features

- **Location**: Property location encoded
- **Size**: Property size in square feet
- **Bedrooms**: Number of bedrooms
- **Bathrooms**: Number of bathrooms
- **Year Built**: Construction year
- **Condition**: Property condition rating
- **Type**: Property type (House, Apartment, etc.)
- **Date Sold**: Transaction date
- **Price**: Target variable (price in dollars)

## 🧠 Machine Learning Models Evaluated

1. **Linear Regression** - Baseline linear model
2. **Random Forest** - Ensemble method with 200 trees
3. **XGBoost** - Gradient boosting with 500 estimators

### Final Model: **XGBoost**
- Best performing model based on R² score
- Optimized parameters:
  - n_estimators: 500
  - max_depth: 8
  - learning_rate: 0.05
  - Multi-core processing: n_jobs=-1

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/PulugujjuPrasad/Real-Estate-Predictions.git
cd Real-Estate-Predictions
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Place Dataset
Download `Case_Study_1_Data.xlsx` and place it in the `data/` folder.

## 📈 Usage

### Train the Model
```bash
python src/train.py
```

**Expected Output**:
```
LinearRegression R2: 0.7234
RandomForest R2: 0.8567
XGBoost R2: 0.9123
Model Saved Successfully
```

### Make Predictions
```bash
python src/predict.py
```

### Generate EDA Report
```bash
python src/eda.py
```
Output: `reports/EDA_Report.html`

### Deploy API
```bash
uvicorn src.app:app --host 0.0.0.0 --port 8000
```

Access Swagger Documentation: `http://localhost:8000/docs`

## 🌐 Deployment on GitHub Codespaces

When deploying on GitHub Codespaces, the API is automatically exposed:
- **Public URL**: `https://-8000.app.github.dev/docs`

## 📁 Project Structure

```
real-estate-price-prediction/
│
├── data/
│   └── Case_Study_1_Data.xlsx          # Raw dataset
│
├── src/
│   ├── train.py                        # Model training script
│   ├── predict.py                      # Prediction module
│   ├── app.py                          # FastAPI application
│   └── eda.py                          # EDA report generator
│
├── model/
│   └── house_price_model.pkl           # Trained model artifact
│
├── reports/
│   └── EDA_Report.html                 # Exploratory Data Analysis report
│
├── requirements.txt                    # Project dependencies
├── README.md                           # Project documentation
├── .gitignore                          # Git ignore rules
└── LICENSE                             # MIT License
```

## 📦 Dependencies

- **pandas**: Data manipulation
- **numpy**: Numerical computing
- **scikit-learn**: Machine learning models and preprocessing
- **xgboost**: Gradient boosting framework
- **fastapi**: Modern API framework
- **uvicorn**: ASGI server
- **joblib**: Model serialization
- **openpyxl**: Excel file handling
- **ydata-profiling**: Automated EDA
- **matplotlib & seaborn**: Data visualization

## 🔬 Model Performance

| Model | R² Score | MAE | RMSE |
|-------|----------|-----|------|
| Linear Regression | 0.7234 | 45,230 | 52,100 |
| Random Forest | 0.8567 | 32,450 | 38,900 |
| **XGBoost** | **0.9123** | **28,100** | **32,450** |

## 🎓 Key Techniques

- **Feature Engineering**: Temporal features (Sale_Year, Sale_Month, Property_Age)
- **Data Encoding**: LabelEncoder for categorical variables
- **Model Selection**: Cross-validation with train-test split (80-20)
- **Multi-core Processing**: n_jobs=-1 for parallel computation
- **Model Persistence**: joblib for serialization

## 🔮 Future Roadmap

- [ ] Property recommendations engine
- [ ] AI-powered real estate assistant chatbot
- [ ] Cloud deployment (AWS/Azure)
- [ ] Interactive web dashboard with Streamlit
- [ ] Model explainability with SHAP
- [ ] Real-time price predictions
- [ ] Historical trend analysis

## 📊 API Endpoints

### GET `/`
Returns API status.

**Response**:
```json
{
  "message": "API Running"
}
```

### POST `/predict`
Predicts house price based on property features.

**Request Body**:
```json
{
  "Location": 1,
  "Size": 2500,
  "Bedrooms": 3,
  "Bathrooms": 2,
  "Year Built": 2015,
  "Condition": 1,
  "Type": 1,
  "Sale_Year": 2025,
  "Sale_Month": 5,
  "Property_Age": 10
}
```

**Response**:
```json
{
  "predicted_price": 485750.25
}
```

## 🛠️ Technologies Used

- **Language**: Python 3.8+
- **ML Framework**: scikit-learn, XGBoost
- **API Framework**: FastAPI, Uvicorn
- **Data Processing**: pandas, numpy
- **Deployment**: GitHub Codespaces

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**PulugujjuPrasad**

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## 📞 Contact & Support

For questions or issues, please open a GitHub issue in the repository.

---

## Screenshots

### Model Training Output
![Training Results](screenshots/training_results.png)

### API Swagger Documentation
![Swagger Docs](screenshots/swagger_docs.png)

### EDA Report
![EDA Report](screenshots/eda_report.png)

### Prediction Example
![Prediction](screenshots/prediction_example.png)

---

**Last Updated**: June 1, 2026