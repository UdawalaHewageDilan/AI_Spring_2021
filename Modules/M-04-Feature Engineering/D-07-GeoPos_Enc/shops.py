import pandas as pd
import numpy as np
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import plotly.express as px
import plotly.graph_objects as go
import cufflinks as cf
import plotly.io as pio
from plotly.io import orca
import plotly.offline as pyo

from plotly.offline import download_plotlyjs, plot, iplot
cf.go_offline()
pio.renderers.default = 'png'

df_shops = pd.read_csv('shops.csv')

df_shops['city'] = df_shops['shop_name'].apply(
    lambda x: x.replace('!', '').strip().split()[0]
)

#address = df_shops.iloc[2, 0]

#address_geo = Nominatim(user_agent='tutorial').geocode(address)

geocoder = RateLimiter(Nominatim(user_agent='tutorial').geocode, min_delay_seconds=1)


df_shops['locations'] = df_shops['city'].apply(geocoder)

# geocoder2 = RateLimiter(Nominatim(user_agent='tutorial').geocode, min_delay_seconds=1)
df_shops['city_long'] = df_shops['locations'].apply(
    lambda loc: loc.longitude if loc else None
)

df_shops['city_lat'] = df_shops['locations'].apply(
    lambda loc: loc.latitude if loc else None
)


fig = px.density_mapbox(df_shops, lat='city_lat', lon='city_long', radius=5, hover_name='city', mapbox_style='open-street-map')
pyo.plot(fig)

#fig2 = px.scatter_geo()