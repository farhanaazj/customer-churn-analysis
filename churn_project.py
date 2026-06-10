# ================================
# CUSTOMER CHURN PREDICTION PROJECT
# ================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib
import sqlite3

# ================================
# 1. LOAD DATA
# ================================

df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("\nDataset Shape:", df.shape)
print(df.head())

# ================================
# 2. CLEAN DATA
# ================================

# Convert TotalCharges to numeric
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())

# Drop customerID (useless for ML)
df.drop('customerID', axis=1, inplace=True)

# Convert target variable
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

# ================================
# 3. BASIC ANALYSIS
# ================================

print(f"\nChurn Rate: {df['Churn'].mean() * 100:.2f}%")

# Plot churn
sns.countplot(x='Churn', data=df)
plt.title("Churn Distribution")
plt.show()

# ================================
# 4. ENCODE CATEGORICAL DATA
# ================================

df_encoded = pd.get_dummies(df, drop_first=True)

# ================================
# 5. SPLIT DATA
# ================================

X = df_encoded.drop('Churn', axis=1)
y = df_encoded['Churn']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ================================
# 6. MODEL TRAINING
# ================================

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# ================================
# 7. PREDICTIONS
# ================================

y_pred = model.predict(X_test)

# ================================
# 8. EVALUATION
# ================================

accuracy = accuracy_score(y_test, y_pred)

print(f"\nAccuracy: {accuracy*100:.2f}%")

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:\n", cm)

# Confusion Matrix Visualization
plt.figure(figsize=(6,4))

sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=['No Churn', 'Churn'],
    yticklabels=['No Churn', 'Churn']
)

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()

plt.show()

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# ================================
# 9. FEATURE IMPORTANCE
# ================================

importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.feature_importances_
}).sort_values(by='Importance', ascending=False)

print("\nTop 10 Important Features:\n")
print(importance.head(10))

top10 = importance.head(10).copy()

# Cleaner feature names
top10['Feature'] = top10['Feature'].replace({
    'TotalCharges': 'Total Charges',
    'MonthlyCharges': 'Monthly Charges',
    'tenure': 'Tenure',
    'PaymentMethod_Electronic check': 'Electronic Check',
    'InternetService_Fiber optic': 'Fiber Optic',
    'Contract_Two year': 'Two-Year Contract',
    'gender_Male': 'Gender (Male)',
    'OnlineSecurity_Yes': 'Online Security',
    'PaperlessBilling_Yes': 'Paperless Billing',
    'Partner_Yes': 'Partner'
})

# Plot feature importance
plt.figure(figsize=(12,6))

sns.barplot(x='Importance', y='Feature', data=top10)
plt.title("Top Features Affecting Churn")
plt.subplots_adjust(left=0.30)
plt.tight_layout()
plt.show()

# ================================
# 10. SAVE MODEL
# ================================

joblib.dump(model, "models/churn_model.pkl")
joblib.dump(X.columns, "models/model_features.pkl")

print("\nModel saved successfully!")

# ================================
# 11. SQL PART (LOCAL DATABASE)
# ================================

conn = sqlite3.connect("sql/churn.db")
df.to_sql("customers", conn, if_exists="replace", index=False)

query = """
SELECT Contract,
       COUNT(*) AS total_customers,
       SUM(Churn) AS churned_customers
FROM customers
GROUP BY Contract;
"""

result = pd.read_sql(query, conn)

print("\nSQL Result:\n", result)

# ================================
# END OF PROJECT
# ================================