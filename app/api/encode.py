import pandas as pd

def encode(X_new: pd.DataFrame):
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
    
    return X_new