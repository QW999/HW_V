import requests
import json
import pprint

pp = pprint.PrettyPrinter(indent=2)

# import date
#
# string = "14 Feb 2021"
# date = date.date.strptime(string, "%d %b %Y")


Asteroids_Neo_Feed = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=2021-02-14&end_date=2021-02-14&api_key=vh4MyOD88FqMEgCpPK8dM1VVJqkpRf8h6wyAWplK'

# url_Asteroids = 'https://api.nasa.gov/neo/rest/v1/feed?'
# API_Asteroids = 'vh4MyOD88FqMEgCpPK8dM1VVJqkpRf8h6wyAWplK'

# # start_date = input('start_date=')
# start_date = 'start_date=2021-02-14'
# # end_date = input('end_date=')
# end_date = 'end_date=2021-02-14'

# Asteroids_Neo_Feed = 'https://api.nasa.gov/neo/rest/v1/feed?' + 'start_date' + '&' + 'end_date' + '&api_key=' + 'vh4MyOD88FqMEgCpPK8dM1VVJqkpRf8h6wyAWplK'



response_2 = requests.get(Asteroids_Neo_Feed)
data_2 = json.loads(response_2.text)
pp.pprint(data_2)