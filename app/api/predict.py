import logging
import random
import joblib
import app.api.encode as ec

from fastapi import APIRouter
import pandas as pd
from sklearn.model_selection import RandomizedSearchCV
from pydantic import BaseModel, Field, validator
from tensorflow import keras

log = logging.getLogger(__name__)
router = APIRouter()


class Item(BaseModel):
    """Use this data model to parse the request body JSON."""

    borough: str = Field(..., example = 'Manhattan')
    neighbourhood: str = Field(..., example = 'Midtown')
    room_type: str = Field(..., example = 'Entire home/apt')
    latitude: float = Field(..., example = 40)
    longitude: float = Field(..., example = -73)

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

    def encode(self):
        bdict, ndict, rdict = ec.encode_dict()
        self.borough = bdict[self.borough]
        self.neighbourhood = ndict[self.neighbourhood]
        self.room_type = rdict[self.room_type]


@router.post('/predict')
async def predict(item: Item):
    """
    Make random baseline predictions for classification problem 🔮

    ### Request Body
    - `borough`: string
    - `neighbourhood`: string
    - `room_type`: string
    - `latitude`: float
    - `longitude`: float

    ### Response
    - `prediction`: boolean, at random
    - `predict_proba`: float between 0.5 and 1.0, 
    representing the predicted class's probability

    Replace the placeholder docstring and fake predictions with your own model.
    """
    
    item.encode()
    X_new = item.to_df()
    
    # Predict
    model = keras.models.load_model('./assets/EarlyStopping+L2_WeightDecay/saved_model.pb')
    
    y_pred = model.predict(X_new)
    y_pred_proba = random.random() / 2 + 0.5
    return {
        'prediction': y_pred[0],
        'probability': y_pred_proba,
    }
