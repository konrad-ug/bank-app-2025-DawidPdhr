from src.account import Account


class TestAccount:
    def test_account_creation(self):
        account = Account("John", "Doe", "12345678910")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0.0
        assert account.pesel == "12345678910"
    
    def test_pesel_too_short(self):
        account = Account("John", "Doe", "12345")
        assert account.pesel == "Invalid"
    
    def test_pesel_too_long(self):
        account = Account("John", "Doe", "123456789101112131415")
        assert account.pesel == "Invalid"
    
    def test_pesel_non_digit(self):
        account = Account("John", "Doe", None)
        assert account.pesel == "Invalid"

    def test_promo_code_too_long(self):
        account = Account("John", "Doe", "12345678910", "PROM_RABAT")
        assert account.balance == 0.0
    
    def test_promo_code_too_short(self):
        account = Account("John", "Doe", "12345678910", "PROM_X")
        assert account.balance == 0.0