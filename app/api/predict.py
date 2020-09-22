import logging
import random
import joblib

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator

log = logging.getLogger(__name__)
router = APIRouter()


class Item(BaseModel):
    """Use this data model to parse the request body JSON."""

    borough: str = Field(..., example = 'Manhattan')
    neighbourhood: str = Field(..., example = 'Midtown')
    room_type: str = Field(..., example = 'Entire home/apt')

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

    # @validator('x1')
    # def x1_must_be_positive(cls, value):
    #     """Validate that x1 is a positive number."""
    #     assert value > 0, f'x1 == {value}, must be > 0'
    #     return value


@router.post('/predict')
async def predict(item: Item):
    """
    Make random baseline predictions for classification problem 🔮

    ### Request Body
    - `x1`: positive float
    - `x2`: integer
    - `x3`: string

    ### Response
    - `prediction`: boolean, at random
    - `predict_proba`: float between 0.5 and 1.0, 
    representing the predicted class's probability

    Replace the placeholder docstring and fake predictions with your own model.
    """

    X_new = item.to_df()
    log.info(X_new)
    
    # Create all the dictionaries
    df = pd.read_csv('./assets/listings.csv')
    
    def create_dict(borough: str):
        select = df[df['borough'] == str]
        unique = select['neighbourhood'].unique()
        dct = {}
        for element in unique:
            dct['Bronx'] = element
        
        return dct
    
    bronx_dict = create_dict('Bronx')
    brooklyn_dict = create_dict('Brooklyn')
    manhattan_dict = create_dict('Manhattan')
    queens_dict = create_dict('Queens')
    staten_island_dict = create_dict('Staten Island')
    
    # Encode
    blist1 = pd.factorize(df['borough'], sort = True)[1]
    borough_dict = {}
    for i in range(len(blist1)):
        borough_dict[blist1[i]] = i
    
    nlist1 = pd.factorize(df['neighbourhood'], sort = True)[1]
    neighbourhood_dict = {}
    for i in range(len(nlist1)):
        neighbourhood_dict[nlist1[i]] = i
    
    rlist1 = pd.factorize(df['room_type'], sort = True)[1]
    room_type_dict = {}
    for i in range(len(rlist1)):
        room_type_dict[rlist1[i]] = i
    
    blist2 = pd.factorize(df['borough'], sort = True)[0]
    X_new['borough'] = blist2
    
    nlist2 = pd.factorize(df['neighbourhood'], sort = True)[0]
    X_new['neighbourhood'] = nlist2
    
    rlist2 = pd.factorize(df['room_type'], sort = True)[0]
    X_new['room_type'] = rlist2
    
    # Predict
    model = joblib.load('./assets/model.joblib')
    
    y_pred = model.predict(X_new)
    return {
        'prediction': y_pred
    }


