import requests
import time

create_job_url = "https://playground.learnqa.ru/ajax/api/longtime_job"
create_job_response = requests.get(create_job_url)
response_data = create_job_response.json()
token = response_data["token"]
seconds = response_data["seconds"]

print(f"Задача создана с токеном: {token}, и будет выполнена через {seconds} секунд")

check_status_url = f"{create_job_url}?token={token}"
check_status_response = requests.get(check_status_url)
status_data = check_status_response.json()
status = status_data["status"]
print(f"Статус задачи до ожидания: {status}")

time.sleep(seconds)

check_status_response = requests.get(check_status_url)
status_data = check_status_response.json()
status = status_data["status"]
if status == "Job is ready":
    result = status_data["result"]
    print(f"Статус задачи после ожидания: {status}")
    print(f"Результат задачи: {result}")
else:
    print(f"Статус задачи после ожидания: {status}")
