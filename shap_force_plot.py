# SHAP Force Plot for individual patient explanation
# Making our PCOS model transparent, one prediction at a time 💖

import shap
import pandas as pd
import joblib
import numpy as np
import os

# Enable interactive JS plots
shap.initjs()

# Load trained model
model = joblib.load("model/pcos_random_forest_model.pkl")

# Load and clean dataset
df = pd.read_csv("PCOS_final_dataset.csv")
X = df.drop("PCOS (Y/N)", axis=1)
X['AMH(ng/mL)'] = pd.to_numeric(X['AMH(ng/mL)'], errors='coerce')
X.dropna(subset=['AMH(ng/mL)'], inplace=True)

# Get SHAP values
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)
shap_values_class1 = shap_values[:, :, 1]  # class 1 = PCOS

# lets Pick some patients to explain
for i in range(5):
    patient_data = X.iloc[i]
    patient_shap = shap_values_class1[i]

    force_plot = shap.force_plot(
        explainer.expected_value[1],
        patient_shap,
        patient_data
    )

    shap.save_html(f"shap_outputs/force_plot_patient{i}.html", force_plot)

print(f"✅ Saved: shap_outputs/force_plot_patient{i}.html")
