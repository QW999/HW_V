import requests
import json
import pprint

pp = pprint.PrettyPrinter(indent=2)


NASA_APIs = 'https://api.nasa.gov/planetary/apod?api_key=eHv7Q0ZedKx7JwWVhYooeev0RAoLshLAWyUuKbm4'
# APIs_key = 'eHv7Q0ZedKx7JwWVhYooeev0RAoLshLAWyUuKbm4'
# NASA_url = 'https://api.nasa.gov/planetary/apod?api_key='

response = requests.get(NASA_APIs)
data = json.loads(response.text)
# pp.pprint(data)

# print(data['title'])
# print('current_date: ', data['date'])
# print('url: ', data['url'])


Asteroids_Neo_Feed = 'https://api.nasa.gov/planetary/apod?api_key=vh4MyOD88FqMEgCpPK8dM1VVJqkpRf8h6wyAWplK'
response_2 = requests.get(Asteroids_Neo_Feed)
data_2 = json.loads(response_2.text)
pp.pprint(data_2)