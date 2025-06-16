from package.models.schema import PredictRequest
from package.utils.loader import load_model
import numpy as np

model = load_model()

def predict_thyroid(data: PredictRequest) -> int:
    input_array = np.array([[
        data.age,
        data.sex,
        data.on_thyroxine,
        data.TSH,
        data.T3,
        data.TT4,
        data.T4U,
        data.FTI,
        data.referral_source
    ]])
    
    prediction = model.predict(input_array)[0]

    # Get probabilities
    probas = model.predict_proba(input_array)

    return probas, int(prediction)
