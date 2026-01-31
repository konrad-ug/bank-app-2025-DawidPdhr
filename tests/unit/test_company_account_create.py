from src.company_account import CompanyAccount


class TestCompanyAccount:
    def test_account_creation(self, mocker):
        mocker.patch(
            "src.company_account.CompanyAccount.does_nip_exist", return_value=True
        )
        account = CompanyAccount("Amuse Incorporated", "1234567890")
        assert account.company_name == "Amuse Incorporated"
        assert account.balance == 0.0
        assert account.nip == "1234567890"

    def test_nip_too_short(self):
        account = CompanyAccount("Amuse Incorporated", "12345")
        assert account.nip == "Invalid"

    def test_nip_too_long(self):
        account = CompanyAccount("Amuse Incorporated", "123456789101112131415")
        assert account.nip == "Invalid"

    def test_nip_non_digit(self):
        account = CompanyAccount("Amuse Incorporated", None)
        assert account.nip == "Invalid"
