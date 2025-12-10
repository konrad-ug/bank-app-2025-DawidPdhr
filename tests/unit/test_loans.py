import pytest
from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount

class TestPersonalLoans:
    @pytest.fixture(autouse=True)
    def account(self):
        return PersonalAccount("John", "Doe", "12345678910")

    @pytest.mark.parametrize("history, amount, expected_result, expected_balance", [
        ([200.0, 300.0, 100.0], 1000.0, True, 1000.0),
        ([200.0, 300.0, 100.0, -150.0, -50.0], 300.0, True, 300.0),
        ([200.0, -300.0, 100.0], 1000.0, False, 0.0),
        ([200.0, 300.0, 100.0, -150.0, -50.0], 500.0, False, 0.0),
        ([-200.0, -300.0, 100.0, 150.0, 50.0], 750.0, True, 750.0),
        ([200.0, 300.0, 100.0], -300.0, False, 0.0),
        ([200.0, 300.0, 100.0], True, False, 0.0),
        ([200.0, 300.0], 250.0, False, 0.0),
        ([-200.0, 300.0, 150.0, 200.0], 250.0, True, 250.0),
        ([-200.0, 300.0, -150.0, 200.0], 250.0, False, 0.0)
    ],
    ids=[
        "three incoming transfers",
        "sum of five transactions",
        "three transactions not all incoming",
        "sum of five transactions less than loan",
        "last three of five transactions incoming",
        "negative",
        "not number",
        "two transactions",
        "four transactions success",
        "four transactions fail"
    ])
    def test_personal_loan(self, account, history, amount, expected_result, expected_balance):
        account.history = history
        result = account.submit_for_loan(amount)
        assert result == expected_result
        assert account.balance == expected_balance


class TestBusinessLoans:
    @pytest.fixture(autouse=True)
    def account(self):
        return CompanyAccount("Amuse Incorporated", "1234567890")
    
    @pytest.mark.parametrize("history, balance, amount, expected_result, expected_balance", [
        ([-1775.0, 300.0, 100.0], 4000.0, 1000.0, True, 5000.0),
        ([-1775.0, 300.0, 100.0], 2000.0, 1000.0, True, 3000.0),
        ([-1775.0, 300.0, 100.0, -150.0, -50.0], 550.0, 300.0, False, 550.0),
        ([-500.0, -300.0, 100.0], 4000.0, 1000.0, False, 4000.0),
        ([-1775.0, 300.0, 100.0], 2000.0, -300.0, False, 2000.0),
        ([-1775.0, 300.0, 100.0], 2000.0, True, False, 2000.0),
    ],
    ids=[
        "high enough balance",
        "barely high enough balance",
        "too low balance",
        "lack of ZUS transfer",
        "negative",
        "not number",
    ])
    def test_business_loan(self, account, history, balance, amount, expected_result, expected_balance):
        account.history = history
        account.balance = balance
        result = account.take_loan(amount)
        assert result == expected_result
        assert account.balance == expected_balance