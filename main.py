import requests


def get_text_from_url(url_text):
    response = requests.get(url_text)

    if response.status_code == 200:
        content = response.text
        return content
    else:
        print(f"Request failed with status code: {response.status_code}")
        return None


url = "https://playground.learnqa.ru/api/get_text"
response_content = get_text_from_url(url)

if response_content is not None:
    print("Response content:")
    print(response_content)
