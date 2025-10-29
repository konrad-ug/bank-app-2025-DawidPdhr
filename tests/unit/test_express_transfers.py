from src.company_account import CompanyAccount
from src.personal_account import PersonalAccount

class TestCompanyExpressTransfers:
    def test_outgoing_company_express_transfer(self):
        account = CompanyAccount("Amuse Incorporated", "1234567890")
        account.balance = 100.0
        account.outgoing_express_transfer(75.0)
        assert account.balance == 20.0

    def test_outgoing_company_express_transfer_negative_amount(self):
        account = CompanyAccount("Amuse Incorporated", "1234567890")
        account.outgoing_express_transfer(-75.0)
        assert account.balance == 0.0

    def test_outgoing_company_express_transfer_exceeding_balance(self):
        account = CompanyAccount("Amuse Incorporated", "1234567890")
        account.balance = 100.0
        account.outgoing_express_transfer(175.0)
        assert account.balance == 100.0
    
    def test_outgoing_company_express_transfer_exceeding_balance_by_fee(self):
        account = CompanyAccount("Amuse Incorporated", "1234567890")
        account.balance = 100.0
        account.outgoing_express_transfer(100.0)
        assert account.balance == -5.0


class TestPersonalExpressTransfers:
    def test_outgoing_personal_express_transfer(self):
        account = PersonalAccount("John", "Doe", "12345678910")
        account.balance = 100.0
        account.outgoing_express_transfer(75.0)
        assert account.balance == 24.0

    def test_outgoing_personal_express_transfer_negative_amount(self):
        account = PersonalAccount("John", "Doe", "12345678910")
        account.outgoing_express_transfer(-75.0)
        assert account.balance == 0.0

    def test_outgoing_personal_express_transfer_exceeding_balance(self):
        account = PersonalAccount("John", "Doe", "12345678910")
        account.balance = 100.0
        account.outgoing_express_transfer(175.0)
        assert account.balance == 100.0
    
    def test_outgoing_personal_express_transfer_exceeding_balance_by_fee(self):
        account = PersonalAccount("John", "Doe", "12345678910")
        account.balance = 100.0
        account.outgoing_express_transfer(100.0)
        assert account.balance == -1.0