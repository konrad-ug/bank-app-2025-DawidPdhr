import pytest
import requests


class TestAPI:
    url = "http://localhost:5000/api/accounts"

    @pytest.fixture(autouse=True)
    def set_up(self):
        response = requests.post(
            self.url,
            json={"first_name": "John", "last_name": "Doe", "pesel": "12345678910"},
        )
        assert response.status_code == 201
        yield
        accounts = requests.get(self.url).json()
        for account in accounts:
            requests.delete(f'{self.url}/{account["pesel"]}')

    def test_create_account(self):
        payload = {"first_name": "Jane", "last_name": "Doe", "pesel": "10987654321"}
        response = requests.post(self.url, json=payload)
        assert response.status_code == 201
        assert response.json()["message"] == "Account created"

    def test_create_account_with_same_pesel(self):
        payload = {"first_name": "John", "last_name": "Doe", "pesel": "12345678910"}
        response = requests.post(self.url, json=payload)
        assert response.status_code == 409
        assert response.json()["message"] == "Account with this pesel already exists"

    def test_get_all_accounts(self):
        response = requests.get(self.url)
        assert response.status_code == 200
        assert response.json() == [
            {
                "first_name": "John",
                "last_name": "Doe",
                "pesel": "12345678910",
                "balance": 0.0,
            }
        ]

    def test_get_account_count(self):
        url = f"{self.url}/count"
        response = requests.get(url)
        assert response.status_code == 200
        assert response.json()["count"] == 1

    @pytest.mark.parametrize(
        "pesel, expected_code",
        [
            ("12345678910", 200),
            ("10987654321", 404),
        ],
        ids=["Account exists", "Account does not exist"],
    )
    def test_get_account_by_pesel(self, pesel, expected_code):
        url = f"{self.url}/{pesel}"
        response = requests.get(url)
        assert response.status_code == expected_code

    @pytest.mark.parametrize(
        "pesel, first_name, last_name, expected_code",
        [
            ("12345678910", "Johannes", "Douglas", 200),
            ("12345678910", "Johannes", None, 200),
            ("12345678910", None, "Douglas", 200),
            ("12345678910", None, None, 200),
            ("10987654321", "Johannes", "Douglas", 404),
        ],
        ids=[
            "Update first and last name",
            "Update only first name",
            "Update only last name",
            "Update none but account exists",
            "Account does not exist",
        ],
    )
    def test_update_account(self, pesel, first_name, last_name, expected_code):
        url = f"{self.url}/{pesel}"
        payload = {
            "first_name": first_name,
            "last_name": last_name,
        }
        response = requests.patch(url, json=payload)

        assert response.status_code == expected_code

        if expected_code == 200:
            response = requests.get(url)
            assert response.status_code == 200
            if first_name:
                assert response.json()["first_name"] == first_name
            if last_name:
                assert response.json()["last_name"] == last_name

    @pytest.mark.parametrize(
        "pesel, expected_code",
        [
            ("10987654321", 404),
            ("12345678910", 200),
        ],
        ids=[
            "Account does not exist",
            "Account deleted successfully",
        ],
    )
    def test_delete_account(self, pesel, expected_code):
        url = f"{self.url}/{pesel}"
        response = requests.delete(url)
        assert response.status_code == expected_code

    def test_succesfull_delete_account(self):
        url = f"{self.url}/12345678910"
        response = requests.delete(url)
        assert response.status_code == 200

        response = requests.delete(url)
        assert response.status_code == 404
