import pandas as pd
import plotly.graph_objs as gobj
from plotly.offline import iplot
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get('/viz')
async def viz(statecode: str):
    path = './assets/listings.csv'

    df = pd.read_csv(path)

    cols = ['neighbourhood_group','price']

    data = dict(type = 'choropleth',
                locations = df['neighbourhood_group'],
                locationmode = 'USA-states',
                autocolorscale = False,
                colorscale = 'RdBu',
                text= df['neighbourhood_group'],
                z=df['price'],
                marker = dict(line = dict(color = 'rgb(255,255,255)',width = 1)),
                colorbar = {'title':'Colorbar Title','len': 0.25,'lenmode':'fraction'})

    layout = dict(geo = dict(scope='usa'))

    ny_map = gobj.Figure(data = [data],layout = layout)

    return ny_map
