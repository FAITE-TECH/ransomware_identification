import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("../dataset/cleaned.csv")

# Drop list-like columns
drop_cols = [
    "DllCharacteristics",
    "text_Characteristics",
    "rdata_Characteristics"
]

df = df.drop(columns=drop_cols, errors="ignore")

# Encode categorical columns
for col in df.select_dtypes(include="object").columns:
    if col != "Class":
        df[col] = LabelEncoder().fit_transform(df[col].astype(str))

df.to_csv("../dataset/final.csv", index=False)

print("✅ preprocessing completed")