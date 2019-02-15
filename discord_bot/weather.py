import requests
from pprint import pprint

url = 'http://api.openweathermap.org/data/2.5/weather?q=Fairfax,us&appid=ac7c75b9937a495021393024d0a90c44'

res = requests.get(url)

data = res.json()

print(data)




temp = data['main']['temp']
wind_speed = data['wind']['speed']

latitude = data['coord']['lat']
longitude = data['coord']['lon']

description = data['weather'][0]['description']

print('Temperature : {} degree celcius'.format(temp))
print('Wind Speed : {} m/s'.format(wind_speed))
print('Latitude : {}'.format(latitude))
print('Longitude : {}'.format(longitude))
print('Description : {}'.format(description))