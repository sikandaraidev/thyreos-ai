from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.templating import Jinja2Templates
import os
import numpy as np

# from dependencies import get_token_header
from package.models.schema import PredictRequest, PredictResponse
from package.services.predict import predict_thyroid
from package.utils.loader import load_class_names



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "..", "templates"))


# Define the router for prediction-related endpoints
router = APIRouter(
    # prefix="/api/v1",
    # tags=["predict"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)


diagnosis_class = load_class_names()



# def get_current_user(request: Request):
#     user = request.session.get("user")
#     if not user:
#         raise HTTPException(status_code=401, detail="Unauthorized")
#     return user


@router.post("/predict",
    response_model=PredictResponse,
    summary="Predict thyroid condition",
    description="Endpoint to predict thyroid condition based on input features.")
async def predict(request: PredictRequest):
    prob, pred = predict_thyroid(request)
    label_map = diagnosis_class.get(pred, "Unknown")

    # class_id = np.argmax(prob[0])          # ← the predicted class
    # confidence = prob[0][class_id]
    confidence = np.max(prob[0])          # ← the maximum probability

    return {
        "prediction": pred,
        "label": label_map,
        "confidence": confidence,    }