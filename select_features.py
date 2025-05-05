'''In the raw dataset we have many columns so we need to choose the most related ones
we have to select features among 3 categories:
                        1- lifestyle and physical features
                        2-symptom-based features
                        3-medical & hormonal features'''

import pandas as pd

df = pd.read_csv("PCOS_cleaned_data.csv")
selected_features = [
    'Age (yrs)', 'BMI', 'Fast food (Y/N)', 'Reg.Exercise(Y/N)', 'Weight gain(Y/N)',
    'Cycle(R/I)', 'hair growth(Y/N)', 'Pimples(Y/N)', 'Skin darkening (Y/N)', 'Hair loss(Y/N)',
    'AMH(ng/mL)', 'FSH(mIU/mL)', 'LH(mIU/mL)', 'FSH/LH', 'RBS(mg/dl)',
    'Follicle No. (L)', 'Follicle No. (R)', 'Endometrium (mm)',
    'PCOS (Y/N)'
]

df = df[selected_features]

df.to_csv("PCOS_selected_features.csv", index=False)
print( "now you have the dataset you want🌱")