import requests
import json
import pprint

url = 'https://rickandmortyapi.com/api/character/?page='
data = {}
final = {}
for i in range(34, 38):
    response = requests.get(url=url + str(i))
    data = response.json()['results']
    for i in range(len(data)):
        final[data[i]['id']] = {data[i]['name']: {data[i]['url']: data[i]['episode'][0]}}
pprint.pprint(final)

with open('gg.json', 'w') as outfile:
    json.dump(json.dumps(final, indent=4), outfile)

