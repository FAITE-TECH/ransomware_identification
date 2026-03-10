# api/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
from pathlib import Path

# --------------------------
# 1. Define input schema
# --------------------------
class RansomwareFeatures(BaseModel):
    EntryPoint: int
    magic_number: int
    bytes_on_last_page: int
    pages_in_file: int
    relocations: int
    size_of_header: int
    min_extra_paragraphs: int
    max_extra_paragraphs: int
    init_ss_value: int
    init_sp_value: int
    init_ip_value: int
    init_cs_value: int
    over_lay_number: int
    oem_identifier: int
    address_of_ne_header: int
    SizeOfCode: int
    SizeOfInitializedData: int
    SizeOfUninitializedData: int
    AddressOfEntryPoint: int
    BaseOfCode: int
    BaseOfData: int
    ImageBase: int
    SectionAlignment: int
    FileAlignment: int
    OperatingSystemVersion: int
    ImageVersion: int
    SizeOfImage: int
    SizeOfHeaders: int
    Checksum: int
    SizeofStackReserve: int
    SizeofStackCommit: int
    SizeofHeapCommit: int
    SizeofHeapReserve: int
    LoaderFlags: int
    text_VirtualSize: int
    text_VirtualAddress: int
    text_SizeOfRawData: int
    text_PointerToRawData: int
    text_PointerToRelocations: int
    text_PointerToLineNumbers: int
    rdata_VirtualSize: int
    rdata_VirtualAddress: int
    rdata_SizeOfRawData: int
    rdata_PointerToRawData: int
    rdata_PointerToRelocations: int
    rdata_PointerToLineNumbers: int
    registry_read: int
    registry_write: int
    registry_delete: int
    network_threats: int
    network_dns: int
    network_http: int
    network_connections: int
    processes_monitored: int
    files_text: int
    files_unknown: int
    dlls_calls: int
    apis: int
    encryption_score: float
    system_modification_score: float

# --------------------------
# 2. Initialize FastAPI
# --------------------------
app = FastAPI(title="Ransomware Detection API")

# --------------------------
# 3. Load trained model
# --------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
model_path = BASE_DIR / "models" / "model.pkl"
model = joblib.load(model_path)

# Keep the features used in training
model_features = model.feature_names_in_  # works if scikit-learn >=1.0

# --------------------------
# 4. Prediction endpoint
# --------------------------
@app.post("/predict")
def predict(features: RansomwareFeatures):
    # Convert input to single-row DataFrame
    df = pd.DataFrame([features.dict()])

    # Ensure columns match training features
    df = df.reindex(columns=model_features, fill_value=0)

    # Predict
    prediction = model.predict(df)

    # Return prediction
    return {"prediction": int(prediction[0])}