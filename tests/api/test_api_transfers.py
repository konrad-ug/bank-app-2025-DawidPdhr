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
        assert response.json()["message"] == "Account created"
        response = requests.post(
            f"{self.url}/12345678910/transfer",
            json={"amount": 100.0, "type": "incoming"},
        )
        assert response.status_code == 200
        assert response.json()["message"] == "Zlecenie przyjęto do realizacji"
        yield
        all_accounts = requests.get(self.url).json()
        for account in all_accounts:
            requests.delete(f'{self.url}/{account["pesel"]}')

    @pytest.mark.parametrize(
        "payload, pesel, expected_code, expected_balance",
        [
            ({"amount": 100.0, "type": "incoming"}, "12345678910", 200, 200.0),
            ({"amount": 50.0, "type": "outgoing"}, "12345678910", 200, 50.0),
            ({"amount": 50.0, "type": "express"}, "12345678910", 200, 49.0),
            ({"amount": 100.0, "type": "express"}, "12345678910", 200, -1.0),
            ({"amount": 500.0, "type": "outgoing"}, "12345678910", 422, 100.0),
            ({"amount": 20.0, "type": "incoming"}, "10987654321", 404, 100.0),
            ({"amount": -20.0, "type": "outgoing"}, "12345678910", 422, 100.0),
            ({"amount": -20.0, "type": "incoming"}, "12345678910", 422, 100.0),
            ({"amount": 20.0, "type": "surprise"}, "12345678910", 400, 100.0),
            ({"amount": None, "type": "incoming"}, "12345678910", 400, 100.0),
            ({"type": "incoming"}, "12345678910", 400, 100.0),
            ({"amount": 20.0}, "12345678910", 400, 100.0),
            (
                {"amount": 20.0, "type": "incoming", "pesel": "12345678910"},
                "12345678910",
                200,
                120.0,
            ),
            ({}, "12345678910", 400, 100.0),
        ],
        ids=[
            "incoming transfer",
            "outgoing transfer",
            "express transfer",
            "express gets negative",
            "outgoing too much",
            "account doesn't exist",
            "negative amount outgoing",
            "negative amount incoming",
            "non-recognizable type",
            "bad amount type",
            "payload missing amount",
            "payload missing type",
            "payload contains garbage",
            "empty payload",
        ],
    )
    def test_transfers(self, payload, pesel, expected_code, expected_balance):
        url = f"{self.url}/{pesel}/transfer"
        response = requests.post(url, json=payload)

        assert response.status_code == expected_code

        if expected_code == 200:
            url = f"{self.url}/{pesel}"
            response = requests.get(url)
            account = response.json()
            assert account["balance"] == expected_balance
