import sys
from io import BytesIO
# Этот класс поможет нам сделать картинку из потока байт
from choose_scale import choose_scale

import requests
from PIL import Image

# Пусть наше приложение предполагает запуск:
# python search.py Москва, ул. Ак. Королева, 12
# Тогда запрос к геокодеру формируется следующим образом:
toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:
    print('Ошибка выполнения запроса')
    sys.exit(0)

# Преобразуем ответ в json-объект
json_response = response.json()
# Получаем первый топоним из ответа геокодера.
toponym = json_response["response"]["GeoObjectCollection"][
    "featureMember"][0]["GeoObject"]
# Координаты центра топонима:
toponym_coodrinates = toponym["Point"]["pos"]
# Долгота и широта:
toponym_longitude, toponym_latitude = toponym_coodrinates.split(" ")

b_box = [','.join(toponym["boundedBy"]["Envelope"]["lowerCorner"].split(' ')),
         ','.join(toponym["boundedBy"]["Envelope"]["lowerCorner"].split(' '))]

# Собираем параметры для запроса к StaticMapsAPI:
map_params = {
    "b_box": '~'.join(b_box),
    "l": "map",
    "pt": ','.join([toponym_longitude, toponym_latitude]),
    "z": choose_scale(toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][-1]["kind"])
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
# ... и выполняем запрос
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
    response.content)).show()
# Создадим картинку
# и тут же ее покажем встроенным просмотрщиком операционной системы
