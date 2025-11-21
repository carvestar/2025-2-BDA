import pandas as pd
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap

file_name = './data/seoul-metro-2021.logs.csv'
df_raw = pd.read_csv(file_name)

print('-' * 100)
print(df_raw)