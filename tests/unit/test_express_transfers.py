import pytest
from src.company_account import CompanyAccount
from src.personal_account import PersonalAccount

class TestCompanyExpressTransfers:
    @pytest.fixture(autouse=True)
    def account(self):
        return CompanyAccount("Amuse Incorporated", "1234567890")
    
    @pytest.mark.parametrize("initial_balance, transfer_value, expected_balance", [
        (100.0, 75.0, 20.0),
        (100.0, -75.0, 100.0),
        (100.0, True, 100.0),
        (200.0, 275.0, 200.0),
        (500.0, 500.0, -5.0)
    ],
    ids=[
        "normal transfer",
        "negative value",
        "not number value",
        "exceeding balance",
        "exceeding balance by fee"
    ])
    def test_outgoing_company_express_transfer(self, account, initial_balance, transfer_value, expected_balance):
        account.balance = initial_balance
        account.outgoing_express_transfer(transfer_value)
        assert account.balance == expected_balance


class TestPersonalExpressTransfers:
    @pytest.fixture(autouse=True)
    def account(self):
        return PersonalAccount("John", "Doe", "12345678910")
    
    @pytest.mark.parametrize("initial_balance, transfer_value, expected_balance", [
        (100.0, 75.0, 24.0),
        (100.0, -75.0, 100.0),
        (100.0, True, 100.0),
        (200.0, 275.0, 200.0),
        (500.0, 500.0, -1.0)
    ],
    ids=[
        "normal transfer",
        "negative value",
        "not number value",
        "exceeding balance",
        "exceeding balance by fee"
    ])
    def test_outgoing_personal_express_transfer(self, account, initial_balance, transfer_value, expected_balance):
        account.balance = initial_balance
        account.outgoing_express_transfer(transfer_value)
        assert account.balance == expected_balance