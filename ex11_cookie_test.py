import re

import requests


def test_cookie_test():
    response = requests.get('https://playground.learnqa.ru/api/homework_cookie')

    cookies = response.cookies

    cookie_name = "HomeWork"

    if cookie_name in cookies:
        print(f"\n Cookie {cookie_name} has value: {cookies[cookie_name]}")

        expected_value = "hw_value"
        assert cookies[cookie_name] == expected_value, f"Expected {expected_value} but got {cookies[cookie_name]}"
    else:
        print(f"Cookie {cookie_name} not found in response.")
