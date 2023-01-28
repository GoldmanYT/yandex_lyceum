import requests

response = requests.get("http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=Красная%20площадь,%201&format=json")

json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]

toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
toponym_coordinates = toponym["Point"]["pos"]

print(toponym_address, toponym_coordinates, sep='\n')
