import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

# 1.
response = requests.get(url)
print("1. Запрос без параметра method:")
print(response.text)

# 2.
response = requests.head(url)
print("\n2. HEAD запрос:")
print(response.text)

# 3
response = requests.get(url, params={"method": "GET"})
print("\n3. Запрос с правильным значением method:")
print(response.text)

# 4.
http_methods = ["GET", "POST", "PUT", "DELETE"]
print("\n4. Проверка всех возможных сочетаний:")

for method in http_methods:
    for param_value in http_methods:
        if method == "GET":
            response = requests.get(url, params={"method": param_value})
        elif method == "POST":
            response = requests.post(url, data={"method": param_value})
        elif method == "PUT":
            response = requests.put(url, data={"method": param_value})
        elif method == "DELETE":
            response = requests.delete(url, data={"method": param_value})

        print(f"Запрос: {method} с параметром method={param_value} -> Ответ: {response.text}")

        # Проверка несовпадений
        if "success" in response.text and method != param_value:
            print(f"     Найдено несовпадение! Реальный метод: {method}, параметр method: {param_value}")
