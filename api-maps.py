import requests

cities = list(map(str.strip, input().split(',')))
coords = {}
apikey = "40d1649f-0493-4b70-98ba-98533de7710b"

for city in cities:
    request = f"http://geocode-maps.yandex.ru/1.x/?apikey={apikey}&geocode={city}&format=json"
    response = requests.get(request)

    if response:
        json_response = response.json()
        pos = json_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        coord = float(pos.split()[1])
        coords[city] = coord

print(min(coords.items(), key=lambda x: x[1])[0])
