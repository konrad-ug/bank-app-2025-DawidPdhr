from src.personal_account import PersonalAccount


class TestPersonalAccount:
    def test_account_creation(self):
        account = PersonalAccount("John", "Doe", "12345678910")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0.0
        assert account.pesel == "12345678910"
    
    def test_pesel_too_short(self):
        account = PersonalAccount("John", "Doe", "12345")
        assert account.pesel == "Invalid"
    
    def test_pesel_too_long(self):
        account = PersonalAccount("John", "Doe", "123456789101112131415")
        assert account.pesel == "Invalid"
    
    def test_pesel_non_digit(self):
        account = PersonalAccount("John", "Doe", None)
        assert account.pesel == "Invalid"

    def test_promo_code_suffix_too_long(self):
        account = PersonalAccount("John", "Doe", "12345678910", "PROM_RABAT")
        assert account.balance == 0.0
    
    def test_promo_code_suffix_too_short(self):
        account = PersonalAccount("John", "Doe", "12345678910", "PROM_X")
        assert account.balance == 0.0

    def test_promo_code_prefix_too_long(self):
        account = PersonalAccount("John", "Doe", "12345678910", "PROMO_XYZ")
        assert account.balance == 0.0
    
    def test_promo_code_prefix_too_short(self):
        account = PersonalAccount("John", "Doe", "12345678910", "PRO_XYZ")
        assert account.balance == 0.0
    
    def test_promo_code_invalid_prefix(self):
        account = PersonalAccount("John", "Doe", "12345678910", "ROOM_XYZ")
        assert account.balance == 0.0
    
    def test_promo_code_invalid_infix(self):
        account = PersonalAccount("John", "Doe", "12345678910", "PROM-XYZ")
        assert account.balance == 0.0
    
    def test_promo_code_valid(self):
        account = PersonalAccount("John", "Doe", "12345678910", "PROM_XYZ")
        assert account.balance == 50.0
    
    def test_promo_too_old_19xx(self):
        account = PersonalAccount("John", "Doe", "12045678910", "PROM_XYZ")
        assert account.balance == 00.0
    
    def test_promo_too_old_18xx(self):
        account = PersonalAccount("John", "Doe", "12845678910", "PROM_XYZ")
        assert account.balance == 00.0
    
    def test_promo_too_old_1960(self):
        account = PersonalAccount("John", "Doe", "60045678910", "PROM_XYZ")
        assert account.balance == 00.0
    
    def test_promo_applicable_1961(self):
        account = PersonalAccount("John", "Doe", "61045678910", "PROM_XYZ")
        assert account.balance == 50.0