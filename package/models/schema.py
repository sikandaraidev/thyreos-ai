from pydantic import BaseModel
from enum import IntEnum


class PredictRequest(BaseModel):
    age: int
    sex: int
    on_thyroxine: int
    TSH: float
    T3: float
    TT4: float
    T4U: float
    FTI: float
    referral_source: int

class PredictResponse(BaseModel):
    prediction: int   # The predicted class index
    label: str        # The label corresponding to the predicted class
    confidence: float # The confidence score for the prediction


# multi-class int-type classification: 0-negative, 1-hypo, 2-hyper, 3-other, 4-misc
class ThyroidClass(IntEnum):
    negative = 0
    hypo = 1
    hyper = 2
    other = 3
    misc = 4
