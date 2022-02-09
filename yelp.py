import requests
import json

location = "Los Angeles"
search_term = "skewers"
unix_time = "1616823000"

api_key = "KgX_OYPeUach78boaJfcpg7I7gcOOVeK8DbqgXnFG8Wc5Vp4762Kbmd62Z-vtzFGPdeHlxY1rCzomxkPKx17J3_pkapGYNevXmlFeyiFYyY_b1oDU-xoKuow7bSqX3Yx"


def return_array_of_skewer_restaurants():
    params = {
        'term' : search_term,
        'location' : location,
        'open_at' : unix_time
    }

    headers = {
        'Authorization' : 'Bearer %s' % api_key,
    }

    response = requests.get("https://api.yelp.com/v3/businesses/search", params=params, headers=headers)
    if response.status_code == 200:
       data = response.json()
       for x in data['businesses']:
           print(x['name'])


return_array_of_skewer_restaurants()