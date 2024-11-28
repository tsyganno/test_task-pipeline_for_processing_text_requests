import requests

# Тестирование NLP-пайплайна
response = requests.post("http://127.0.0.1:5000/api/preprocess", json={"text": "Пример текста для обработки."})
print(response.json())

response = requests.post("http://127.0.0.1:5000/api/preprocess", json={"text": "Документ содержит информацию о Python."})
print(response.json())

response = requests.post("http://127.0.0.1:5000/api/preprocess", json={"text": "Здесь можно найти данные об обработке текста."})
print(response.json())

# Тестирование поиска
response = requests.post("http://127.0.0.1:5000/api/search", json={"query": "обработка текста"})
print(response.json())

response = requests.post("http://127.0.0.1:5000/api/search", json={"query": "информация о Python"})
print(response.json())

response = requests.post("http://127.0.0.1:5000/api/search", json={"query": "Данные"})
print(response.json())
