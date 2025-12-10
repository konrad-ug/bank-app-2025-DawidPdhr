import pytest
from src.account_registry import AccountRegistry
from src.personal_account import PersonalAccount


class TestAccountRegistry:
    @pytest.fixture(autouse=True)
    def registry(self):
        return AccountRegistry()

    def test_add_account(self, registry):
        account = PersonalAccount("John", "Doe", "12345678910")
        registry.add_account(account)
        assert registry.accounts == [account]

    def test_add_not_account(self, registry):
        registry.add_account(True)
        registry.add_account(123)
        registry.add_account("abc")
        assert registry.accounts == []

    def test_get_account_by_pesel(self, registry):
        account1 = PersonalAccount("John", "Doe", "12345678910")
        account2 = PersonalAccount("Jane", "Doe", "10987654321")
        registry.add_account(account1)
        registry.add_account(account2)
        retrieved_account = registry.get_account_by_pesel("12345678910")
        assert retrieved_account == account1

    def test_get_account_by_pesel_not_existing(self, registry):
        retrieved_account = registry.get_account_by_pesel("10987654321")
        assert retrieved_account is None

    def test_get_all_accounts(self, registry):
        account1 = PersonalAccount("John", "Doe", "12345678910")
        account2 = PersonalAccount("Jane", "Doe", "10987654321")
        account3 = PersonalAccount("Jack", "Doe", "67891012345")
        account4 = PersonalAccount("Jade", "Doe", "54321109876")
        account5 = PersonalAccount("Jude", "Doe", "12345109876")
        registry.add_account(account1)
        registry.add_account(account2)
        registry.add_account(account3)
        registry.add_account(account4)
        registry.add_account(account5)
        retrieved_accounts = registry.get_all_accounts()
        assert retrieved_accounts == [account1, account2, account3, account4, account5]

    def test_get_number_of_accounts(self, registry):
        account1 = PersonalAccount("John", "Doe", "12345678910")
        account2 = PersonalAccount("Jane", "Doe", "10987654321")
        account3 = PersonalAccount("Jack", "Doe", "67891012345")
        account4 = PersonalAccount("Jade", "Doe", "54321109876")
        account5 = PersonalAccount("Jude", "Doe", "12345109876")
        registry.add_account(account1)
        registry.add_account(account2)
        registry.add_account(account3)
        registry.add_account(account4)
        registry.add_account(account5)
        number_of_accounts = registry.get_number_of_accounts()
        assert number_of_accounts == 5
