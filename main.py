from json.decoder import JSONDecodeError
import requests


def get_text_from_url(url_text, payload):
    response = requests.get(url_text, params=payload)

    if response.status_code == 200:
        content = response.text
        return content
    else:
        print(f"Request failed with status code: {response.status_code}")
        return None


def get_parsed_json():
    response = requests.get("https://playground.learnqa.ru/api/get_text")
    try:
        parsed_response_text = response.json()
        return parsed_response_text
    except JSONDecodeError:
        print("Response is not a JSON format")

def api_test():
    payload = {"email": "email", "password": "password"}
    response = requests.post("https://sc.x5.ru/v2/logistics/auth", payload)
    print(response.status_code)
    print(response.text)


def get_status_code():
    response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
    print(response.status_code)
    print(response.history)


payload = {"name": "User"}
url = "https://playground.learnqa.ru/api/get_301"
response_content = get_text_from_url(url, payload)

if response_content is not None:
    print("Response content:")
    print(response_content)
# print(get_parsed_json())
# get_status_code()
api_test()
