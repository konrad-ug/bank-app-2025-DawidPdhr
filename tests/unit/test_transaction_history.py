from src.company_account import CompanyAccount
from src.personal_account import PersonalAccount

class TestCompanyTransfersHistory:
    def test_fresh_company_history(self):
        account = CompanyAccount("Amuse Incorporated", "1234567890")
        assert account.history == []

    def test_outgoing_company_express_transfer_history(self):
        account = CompanyAccount("Amuse Incorporated", "1234567890")
        account.balance = 100.0
        account.outgoing_express_transfer(75.0)
        assert account.history == [-75.0, -5.0]

    def test_outgoing_company_express_transfer_negative_amount_history(self):
        account = CompanyAccount("Amuse Incorporated", "1234567890")
        account.outgoing_express_transfer(-75.0)
        assert account.history == []

    def test_outgoing_company_express_transfer_exceeding_balance_history(self):
        account = CompanyAccount("Amuse Incorporated", "1234567890")
        account.balance = 100.0
        account.outgoing_express_transfer(175.0)
        assert account.history == []
    
    def test_outgoing_company_express_transfer_exceeding_balance_by_fee_history(self):
        account = CompanyAccount("Amuse Incorporated", "1234567890")
        account.balance = 100.0
        account.outgoing_express_transfer(100.0)
        assert account.history == [-100.0, -5.0]

    def test_company_incoming_transfer_history(self):
        account = CompanyAccount("Amuse Incorporated", "1234567890")
        account.incoming_transfer(75.0)
        assert account.history == [75.0]

    def test_company_incoming_transfer_negative_amount_history(self):
        account = CompanyAccount("Amuse Incorporated", "1234567890")
        account.incoming_transfer(-75.0)
        assert account.history == []

    def test_company_outgoing_transfer_history(self):
        account = CompanyAccount("Amuse Incorporated", "1234567890")
        account.balance = 100.0
        account.outgoing_transfer(75.0)
        assert account.history == [-75.0]

    def test_company_outgoing_transfer_negative_amount_history(self):
        account = CompanyAccount("Amuse Incorporated", "1234567890")
        account.outgoing_transfer(-75.0)
        assert account.history == []

    def test_company_outgoing_transfer_exceeding_balance_history(self):
        account = CompanyAccount("Amuse Incorporated", "1234567890")
        account.balance = 100.0
        account.outgoing_transfer(175.0)
        assert account.history == []
    
    def test_company_incoming_and_express_outgoing_transfer_history(self):
        account = CompanyAccount("Amuse Incorporated", "1234567890")
        account.incoming_transfer(500.0)
        account.outgoing_express_transfer(300.0)
        assert account.history == [500.0, -300.0, -5.0]


class TestPersonalTransfersHistory:
    def test_fresh_personal_history(self):
        account = PersonalAccount("John", "Doe", "12345678910")
        assert account.history == []

    def test_outgoing_personal_express_transfer_history(self):
        account = PersonalAccount("John", "Doe", "12345678910")
        account.balance = 100.0
        account.outgoing_express_transfer(75.0)
        assert account.history == [-75.0, -1.0]

    def test_outgoing_personal_express_transfer_negative_amount_history(self):
        account = PersonalAccount("John", "Doe", "12345678910")
        account.outgoing_express_transfer(-75.0)
        assert account.history == []

    def test_outgoing_personal_express_transfer_exceeding_balance_history(self):
        account = PersonalAccount("John", "Doe", "12345678910")
        account.balance = 100.0
        account.outgoing_express_transfer(175.0)
        assert account.history == []
    
    def test_outgoing_personal_express_transfer_exceeding_balance_by_fee_history(self):
        account = PersonalAccount("John", "Doe", "12345678910")
        account.balance = 100.0
        account.outgoing_express_transfer(100.0)
        assert account.history == [-100.0, -1.0]
    
    def test_personal_incoming_transfer_history(self):
        account = PersonalAccount("John", "Doe", "12345678910")
        account.incoming_transfer(75.0)
        assert account.history == [75.0]

    def test_personal_incoming_transfer_negative_amount_history(self):
        account = PersonalAccount("John", "Doe", "12345678910")
        account.incoming_transfer(-75.0)
        assert account.history == []

    def test_personal_outgoing_transfer_history(self):
        account = PersonalAccount("John", "Doe", "12345678910")
        account.balance = 100.0
        account.outgoing_transfer(75.0)
        assert account.history == [-75.0]

    def test_personal_outgoing_transfer_negative_amount_history(self):
        account = PersonalAccount("John", "Doe", "12345678910")
        account.outgoing_transfer(-75.0)
        assert account.history == []

    def test_personal_outgoing_transfer_exceeding_balance_history(self):
        account = PersonalAccount("John", "Doe", "12345678910")
        account.balance = 100.0
        account.outgoing_transfer(175.0)
        assert account.history == []
    
    def test_personal_incoming_and_express_outgoing_transfer_history(self):
        account = PersonalAccount("John", "Doe", "12345678910")
        account.incoming_transfer(500.0)
        account.outgoing_express_transfer(300.0)
        assert account.history == [500.0, -300.0, -1.0]