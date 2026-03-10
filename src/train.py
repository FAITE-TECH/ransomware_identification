from pathlib import Path
import pandas as pd
import joblib
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(BASE_DIR / "dataset" / "featured.csv")

# Encode label
le = LabelEncoder()
df["Class"] = le.fit_transform(df["Class"])

X = df.drop("Class", axis=1)
y = df["Class"]

# Balance dataset
sm = SMOTE(random_state=42)
X_res, y_res = sm.fit_resample(X, y)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X_res, y_res, test_size=0.2, random_state=42, stratify=y_res
)

# Train
model = RandomForestClassifier(n_estimators=200)
model.fit(X_train, y_train)

# ⭐ create models folder automatically
models_dir = BASE_DIR / "models"
models_dir.mkdir(exist_ok=True)

# Save
joblib.dump(model, models_dir / "model.pkl")
joblib.dump(list(X.columns), models_dir / "features.pkl")
joblib.dump(le, models_dir / "label.pkl")

print("✅ Model trained and saved!")