import requests
import json

url_get = 'https://api.hh.ru/vacancies?area=113' # используемый адрес для отправки запроса

response = requests.get(url_get) # отправка GET-запроса

# print(response) # вывод объекта класса Response
# Вывод:
# >> <Response [200]>

print(response.status_code) # вывод статуса запроса, 200 означает, что всё хорошо, остальные коды нас пока не интересуют и их можно считать показателем ошибки

# Вывод:
# >> 200

print(response.text)
# ensure_ascii=False
# encoding='utf-8'

file = open("vacancies.json", "w")
data = response.text
json.dump(data, file)