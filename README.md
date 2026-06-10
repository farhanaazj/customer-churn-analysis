# 📊 Customer Churn Analysis & Prediction Dashboard

This project analyzes customer churn behavior using the IBM Telco Customer Churn dataset. The objective is to identify churn drivers, predict customer attrition using machine learning, and provide business insights through an interactive Power BI dashboard.

## 🎯 Business Problem
Telecommunication companies lose revenue when customers 
discontinue services. Identifying high-risk customers enables 
businesses to improve retention strategies and reduce churn.

## 🛠️ Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- SQLite
- SQL
- Power BI
- Matplotlib
- Seaborn

## 📌 Project Objectives
- Analyze customer behavior and churn patterns
- Identify key factors influencing customer churn
- Build a machine learning model to predict churn
- Perform SQL-based KPI analysis
- Develop an interactive Power BI dashboard
- Generate actionable business recommendations

## 📂 Dataset Description
- Dataset: IBM Telco Customer Churn Dataset
- Source: Kaggle - https://www.kaggle.com/datasets/blastchar/telco-customer-churn

Dataset Features:
- Customer demographics
- Contract type
- Internet service
- Payment methods
- Monthly charges
- Customer tenure
- Churn status

Target Variable:
- Churn (Yes / No)

## 🧹 Data Preprocessing
- Converted TotalCharges to numeric format
- Handled missing values
- Dropped customerID (non-predictive identifier)
- Encoded churn labels
- Applied one-hot encoding to categorical variables

## 🤖 Machine Learning Model

### Random Forest Classifier
- Ensemble-based classification model
- Handles non-linear relationships effectively
- Used to predict customer churn probability

## 🧪 Model Evaluation

| Metric | Class | Score |
|--------|-------|-------|
| Accuracy | Overall | 79.42% |
| Precision | No Churn | 83% |
| Precision | Churn | 64% |
| Recall | No Churn | 90% |
| Recall | Churn | 50% |
| F1-Score | No Churn | 87% |
| F1-Score | Churn | 56% |

### Confusion Matrix

![Confusion Matrix](images/confusion_matrix.png)

### Feature Importance Analysis

![Feature Importance](images/feature_importance.png)

## 📈 Key Insights
- Month-to-month customers exhibited the highest churn rates
- Fiber optic users demonstrated significantly higher churn compared to DSL users
- Electronic check payment users showed increased churn risk
- Long-tenure customers were more likely to remain with the company
- Higher monthly charges were associated with increased churn

## 📊 Power BI Dashboard

### Churn Overview

![Dashboard Overview](dashboard/dashboard_overview.png)

### Business Insights & Recommendations

![Business Insights](dashboard/business_insights.png)

Dashboard Features:
- KPI Cards
- Churn Analysis Charts
- Interactive Slicers
- Business Insights & Recommendations

## 💡 Business Recommendations
- Encourage customers to switch to long-term contracts
- Improve support quality for fiber optic users
- Promote automatic payment methods
- Launch targeted retention campaigns for high-risk customers

## ▶️ How to Run
1. Clone the repository: git clone <repository-url>
2. Install dependencies: pip install -r requirements.txt
3. Run the Python analysis: python churn_project.py
4. Open the Power BI dashboard: Open dashboard/churn_dashboard.pbix in Power BI Desktop

## 🔮 Future Improvements
- Deploy churn prediction using Streamlit
- Integrate with a cloud database
- Implement automated ETL pipelines
- Add XGBoost and LightGBM models
- Build real-time customer retention monitoring

## 👩‍💻 Author
Farhanaaz J
