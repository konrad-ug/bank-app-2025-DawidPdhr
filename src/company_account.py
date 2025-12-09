from src.account import Account

class CompanyAccount(Account):
    def __init__(self, company_name, nip):
        super().__init__()
        self.company_name = company_name
        self.nip = nip if self.is_nip_valid(nip) else "Invalid"
        self.express_fee = 5.0

    def is_nip_valid(self, nip):
        if isinstance(nip, str) and len(nip) == 10:
            return True
        return False
    
    def outgoing_express_transfer(self, amount):
        return super().outgoing_express_transfer(self.express_fee, amount)
    
    def take_loan(self, amount):
        if isinstance(amount, float) and amount > 0 and -1775.0 in self.history and self.balance >= 2 * amount:
            self.balance += amount
            return True
        return False