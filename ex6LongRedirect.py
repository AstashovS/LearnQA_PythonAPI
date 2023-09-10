import requests


def get_redirects_and_final_url(url):
    response = requests.get(url, allow_redirects=True)

    if not response.history:
        print("Нет редиректов.")
        print(f"Итоговый URL: {response.url}")
        return

    print(f"Количество редиректов: {len(response.history)}")
    for idx, resp in enumerate(response.history, 1):
        print(f"Редирект {idx}: {resp.url}")

    print(f"Итоговый URL: {response.url}")


if __name__ == "__main__":
    url_endpoint = "https://playground.learnqa.ru/api/long_redirect"
    get_redirects_and_final_url(url_endpoint)
