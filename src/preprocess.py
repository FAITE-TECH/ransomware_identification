import pandas as pd
import re

df = pd.read_csv("../dataset/dataset.csv")

# Function to extract hex and convert
def hex_to_int(value):

    if isinstance(value, str):

        # Extract hex pattern
        match = re.search(r'0x[0-9A-Fa-f]+', value)

        if match:
            try:
                return int(match.group(), 16)
            except:
                return value

    return value


# Apply safely
for col in df.select_dtypes(include="object").columns:
    if df[col].astype(str).str.contains("0x").any():
        df[col] = df[col].apply(hex_to_int)

df.to_csv("../dataset/cleaned.csv", index=False)

print("✅ HEX extraction + conversion completed")