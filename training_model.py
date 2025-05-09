# because women's health matters - always ❤️ 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Grab our patients health report 📋
try:
    patient_records = pd.read_csv("PCOS_final_dataset.csv")
    print("Data loaded successfully. Let's dive in!")
except Exception as e:
    print("Something went wrong while loading the data...", e)
    exit()

# Quick fix for that stubborn AMH column (been there, fixed that 😡)
patient_records['AMH(ng/mL)'] = pd.to_numeric(patient_records['AMH(ng/mL)'], errors='coerce')

# Check missing values after conversion
missing_amh = patient_records['AMH(ng/mL)'].isna().sum()
print(f"Missing AMH values after conversion: {missing_amh}")

if missing_amh > 0:
    print("Dropping rows with missing AMH values... bye bye noisy data 🚫")
    patient_records.dropna(subset=['AMH(ng/mL)'], inplace=True)

# Separate features and target variable
patient_features = patient_records.drop('PCOS (Y/N)', axis=1)
pcos_diagnosis = patient_records['PCOS (Y/N)']

# Double check feature types because pandas loves surprises
#print(patient_features.dtypes)

# Train/test split (80/20 because we trust our instincts 🤪)
train_patients, test_patients, train_diagnosis, test_diagnosis = train_test_split(
    patient_features, pcos_diagnosis, test_size=0.2, random_state=42)

# Building a tiny enchanted forest 🌲 (aka RandomForest)
pcos_predictor = RandomForestClassifier(n_estimators=100, random_state=42)
pcos_predictor.fit(train_patients, train_diagnosis)

# Prediction time (Paging Dr. Paria! 👩‍⚕️)
predicted_pcos = pcos_predictor.predict(test_patients)

# Evaluation - how good are we?
accuracy = accuracy_score(test_diagnosis, predicted_pcos)
print(f"\n📈 Model Accuracy: {accuracy:.4f}")

print("\n🔍 Classification Report:")
print(classification_report(test_diagnosis, predicted_pcos))

print("\n🤯 Confusion Matrix:")
print(confusion_matrix(test_diagnosis, predicted_pcos))

# Save the trained model (because retraining is for gym rats not ML queens)
joblib.dump(pcos_predictor, 'pcos_random_forest_model.pkl')
print("\nModel saved as 'pcos_random_forest_model.pkl' - mic drop 🎉")

# Feature Importance (A lil' beauty contest for our clinical features)
feature_importances = pd.Series(pcos_predictor.feature_importances_, index=patient_features.columns)

# Actually sort before plotting!
feature_importances = feature_importances.sort_values()

# Plot (with Paria signature sparkle)
plt.figure(figsize=(12, 8))
colors = plt.cm.PuRd(np.linspace(0.3, 0.9, len(feature_importances)))
feature_importances.plot(
    kind='barh',
    color=colors,
    edgecolor='black',
    alpha=0.8
)
plt.title(
    "Which Factors Predict PCOS Best?",
    fontsize=16,
    color='#AA336A',
    pad=20
)
plt.xlabel("Importance Score (Higher = More Predictive)", fontsize=12)
plt.ylabel("Clinical Features", fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.5)

for spine in ['top', 'right']:
    plt.gca().spines[spine].set_visible(False)

plt.tight_layout()
plt.show()

print("\n🎉 Done and dusted! Keep shining, girl!")
