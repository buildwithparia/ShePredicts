# This file explains our PCOS predictor model
# Let's make the model spill its secrets 🌸

import shap
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np

# Load the trained Random Forest model
pcos_predictor = joblib.load('pcos_random_forest_model.pkl')

# Load the final dataset
patient_records = pd.read_csv('PCOS_final_dataset.csv')

# Prepare X - only features, not the target column
patient_features = patient_records.drop("PCOS (Y/N)", axis=1)

# Clean AMH column (because I faced an error!)
patient_features['AMH(ng/mL)'] = pd.to_numeric(patient_features['AMH(ng/mL)'], errors='coerce')
patient_features.dropna(subset=['AMH(ng/mL)'], inplace=True)

# Initialize the SHAP TreeExplainer
shap_explainer = shap.TreeExplainer(pcos_predictor)

# Calculate SHAP values (returns 3D array: [samples, features, classes])
shap_values = shap_explainer.shap_values(patient_features)

# Select SHAP values for class 1 (PCOS-positive predictions)
shap_values_class1 = shap_values[:, :, 1]

# Plot the summary for class 1
shap.summary_plot(shap_values_class1, patient_features)

shap.initjs()
shap.force_plot(shap_explainer.expected_value[1], shap_values_class1[0], patient_features.iloc[0])

