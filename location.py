from geopy.geocoders import Nominatim
import time
from pprint import pprint

app = Nominatim(user_agent="tutorial")

location = app.geocode("Nairobi, Kenya").raw
# print raw data
pprint(location)