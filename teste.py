import requests
import json
import geocoder	
from decouple import config

#{'lon': -45.4811, 'lat': -7.0219} = g.latlng

key = config("KEY")
g = geocoder.ip('me')

api = f"http://api.openweathermap.org/geo/1.0/reverse?lat={g.lat}&lon={g.lng}&limit=1&appid={key}"
r = requests.get(api)
dados = r.json()

print(g.ip)
print("Seu IP é de: "+dados[0]["name"])
print("OBS: A região localiza as proximidades")