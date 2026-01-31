from src.account import Account
import requests
import datetime

BANK_APP_MF_URL = "https://wl-test.mf.gov.pl"


class CompanyAccount(Account):
    history_email_prefix: str = "Company account history:"

    def __init__(self, company_name, nip):
        super().__init__()
        self.company_name = company_name
        self.nip = nip
        self.express_fee = 5.0

        if self.is_nip_valid(nip):
            if not self.does_nip_exist(nip):
                raise ValueError("Company not registered!")
        else:
            self.nip = "Invalid"

    def is_nip_valid(self, nip):
        if isinstance(nip, str) and len(nip) == 10:
            return True
        return False

    def does_nip_exist(self, nip):
        try:
            response = requests.get(
                f"{BANK_APP_MF_URL}/api/search/nip/{nip}?date={datetime.date.today()}"
            )
            response.raise_for_status()
            data = response.json()

            print(data)

            if (
                data["result"]
                and data["result"]["subject"]
                and data["result"]["subject"]["statusVat"]
            ):
                if data["result"]["subject"]["statusVat"] == "Czynny":
                    return True
            return False

        except requests.RequestException as error:
            print("Api Error:", error)
            return False

    def outgoing_express_transfer(self, amount):
        return super().outgoing_express_transfer(self.express_fee, amount)

    def take_loan(self, amount):
        if (
            isinstance(amount, float)
            and amount > 0
            and -1775.0 in self.history
            and self.balance >= 2 * amount
        ):
            self.balance += amount
            return True
        return False
