import requests


def test_header_test():
    response = requests.get('https://playground.learnqa.ru/api/homework_header')

    headers = response.headers

    header_name = 'x-secret-homework-header'
    expected_value = 'Some secret value'

    if header_name in headers:
        assert headers[header_name] == expected_value, f"Expected {expected_value} but got {headers[header_name]}"
    else:
        assert False, f"Header {header_name} not found in response."
