'''First we need to make data ready for ML'''
import pandas as pd

df = pd.read_csv("PCOS_data.csv")

#remove columns that are useless for our system
df.drop(columns=['Sl. No', 'Patient File No.','Unnamed: 44'], inplace=True)

#fix weird columns name: strip spaces from beginning and end
df.columns = df.columns.str.strip()

'''check if there is missing values'''
missing_rows = df.isnull().sum()

print(missing_rows[missing_rows > 0])

#after running this part I saw we have 2 missing values so:
df['Marraige Status (Yrs)'].fillna(df['Marraige Status (Yrs)'].median(), inplace=True)
df['Fast food (Y/N)'].fillna(df['Fast food (Y/N)'].mode()[0], inplace=True)

#now we save the cleaned data
df.to_csv("PCOS_cleaned_data.csv", index=False)
print( "your cleane data is ready")


