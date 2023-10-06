import json

json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'

# Распарсим строку JSON
data = json.loads(json_text)

# Получим текст второго сообщения
second_message_text = data["messages"][1]["message"]

# Выводим текст второго сообщения
print(second_message_text)