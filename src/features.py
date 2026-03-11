import pandas as pd

df = pd.read_csv("../dataset/final.csv")

df["encryption_score"] = (
    df["files_unknown"]
    + df["dlls_calls"]
    + df["apis"]
    + df["registry_write"]
)

df["system_modification_score"] = (
    df["registry_delete"]
    + df["registry_write"]
)

df.to_csv("../dataset/featured.csv", index=False)

print("✅ feature engineering done")