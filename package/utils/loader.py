import joblib
from pathlib import Path

MODEL_PATH = Path("package/ml_model/model.pkl")
CLASS_PKL_PATH = Path("pkls/class.pkl")

def load_model():
    return joblib.load(MODEL_PATH)

def load_class_names() -> dict:
    return joblib.load(CLASS_PKL_PATH)


# pred=4
# avien = load_class_names()
# label_map = avien.get(pred, "Unknown")

# print(f"label_map: {label_map}")