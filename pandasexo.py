
import numpy as np
import pandas as pd

house = pd.read_csv('./files/house_pricing.csv', ',')
# pd.set_option('display.max_columns', 100)

print(house.describe())