import pandas as pd

def encode_dict():
    df = pd.read_csv('./assets/listings.csv')
    
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
    
    return borough_dict, neighbourhood_dict, room_type_dict
