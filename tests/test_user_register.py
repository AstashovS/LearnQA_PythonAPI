import pytest
import requests

from lib.base_case import BaseCase


class TestUserRegister(BaseCase):
    base_url = "https://playground.learnqa.ru/api/user/"
    def test_create_user_with_existing_email(self):
        email = 'vintikov@example.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        response = requests.post(self.base_url, data=data)

        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    def test_invalid_email(self):
        invalid_email = 'vintikov.example.com'
        data = {
            "username": "user123",
            "firstName": "User",
            "lastName": "Userov",
            "email": invalid_email,
            "password": "password123"
        }
        response = requests.post(self.base_url, data=data)
        assert response.status_code == 400, f"Unexpected status code for email {invalid_email}"

    @pytest.mark.parametrize('missing_field', [
        "username", "firstName", "lastName", "email", "password"
    ])
    def test_missing_field(self, missing_field):
        data = {
            "username": "user123",
            "firstName": "User",
            "lastName": "Userov",
            "email": "user@example.com",
            "password": "password123"
        }
        data.pop(missing_field)  # Удаляем одно из полей
        response = requests.post(self.base_url, data=data)
        assert response.status_code == 400, f"Unexpected status code when missing {missing_field}"

    def test_short_name(self):
        data = {
            "username": "u",
            "firstName": "U",
            "lastName": "Userov",
            "email": "user@example.com",
            "password": "password123"
        }
        response = requests.post(self.base_url, data=data)
        assert response.status_code == 400, "Unexpected status code for short name"

    def test_long_name(self):
        long_name = "A" * 251
        data = {
            "username": long_name,
            "firstName": "User",
            "lastName": "Userov",
            "email": "user@example.com",
            "password": "password123"
        }
        response = requests.post(self.base_url, data=data)
        assert response.status_code == 400, "Unexpected status code for long name"