import numpy as np
import pandas as pd

house = pd.read_csv('./files/houseData.csv')
house_bedrooms = house.groupby(by='bedrooms')
house_id = house.groupby(by='id')

# La moyenne du prix des maisons avec 3 chambres, arrondi a 2 décimal
round(house_bedrooms.get_group(3)['price'].mean(),2)

# Récuperer la colonne prix et bedrooms des maisons avec 3 chambres 
house_bedrooms.get_group(3).loc[:,['price', 'bedrooms']]

# De la ligne 50 à 55 exclu
house.iloc[50:55]

print(house[house['price'] > 1000000])