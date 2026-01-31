from src.account import Account


class PersonalAccount(Account):
    history_email_prefix: str = "Personal account history:"

    def __init__(self, first_name, last_name, pesel, promo_code=None):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 50.0 if self.is_promo_applicable(promo_code, pesel) else 0.0
        self.pesel = pesel if self.is_pesel_valid(pesel) else "Invalid"
        self.express_fee = 1.0

    def is_pesel_valid(self, pesel):
        if isinstance(pesel, str) and len(pesel) == 11:
            return True
        return False

    def is_promo_code_valid(self, promo_code):
        if (
            isinstance(promo_code, str)
            and len(promo_code) == 8
            and promo_code.startswith("PROM_")
        ):
            return True
        return False

    def is_promo_applicable(self, promo_code, pesel):
        if self.is_promo_code_valid(promo_code) and self.is_pesel_valid(pesel):
            if 1 < int(pesel[2]) < 8:
                return True
            if int(pesel[2]) < 2 and int(pesel[:2]) > 60:
                return True
            return False
        return False

    def outgoing_express_transfer(self, amount):
        return super().outgoing_express_transfer(self.express_fee, amount)

    def submit_for_loan(self, amount):
        if isinstance(amount, float) and amount > 0 and len(self.history) > 2:
            if min(self.history[-3:]) > 0 or (
                len(self.history) > 4 and sum(self.history[-5:]) > amount
            ):
                self.balance += amount
                return True
            return False
        return False
