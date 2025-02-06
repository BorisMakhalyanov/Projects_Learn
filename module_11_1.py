from requests import get, ConnectionError

params = {"ll": "108.560751,53.657518",     #вводим координаты места, spn указываем угол места (масштаб охвата поля карты)
          "spn": "3,3",
          "l": "map"}
try:
    response = get("https://static-maps.yandex.ru/1.x/", params=params)
except ConnectionError:
    print("Проверьте подключение к сети.")   #проверка соединения
else:
    with open("map.png", "wb") as file:
        file.write(response.content)

print('картинка места по координатам')
print(params)
print('создана')