import pytest
import requests


class TestPerformance:
    url = "http://localhost:5000/api/accounts"

    def test_create_and_delete_account_performance(self):
        for i in range(100):
            pesel = f"{10000000000 + i}"
            create_response = requests.post(
                self.url,
                json={"first_name": "John", "last_name": "Doe", "pesel": pesel},
                timeout=0.5,
            )

            assert create_response.status_code == 201

            delete_response = requests.delete(f"{self.url}/{pesel}", timeout=0.5)

            assert delete_response.status_code == 200

    def test_incoming_transfers_performance(self):

        requests.post(
            self.url,
            json={"first_name": "John", "last_name": "Doe", "pesel": "12345678910"},
        )

        for _ in range(100):
            response = requests.post(
                f"{self.url}/12345678910/transfer",
                json={"type": "incoming", "amount": 10.0},
                timeout=0.5,
            )
            assert response.status_code == 200

        balance_response = requests.get(f"{self.url}/12345678910")
        assert balance_response.json()["balance"] == 1000
