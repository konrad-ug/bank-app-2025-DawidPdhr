from src.personal_account import PersonalAccount


class AccountRegistry:
    def __init__(self):
        self.accounts: list[PersonalAccount] = []

    def add_account(self, account: PersonalAccount):
        if isinstance(account, PersonalAccount):
            self.accounts.append(account)

    def get_account_by_pesel(self, pesel: str):
        if isinstance(pesel, str):
            for account in self.accounts:
                if account.pesel == pesel:
                    return account
        return None

    def get_all_accounts(self):
        return self.accounts

    def get_number_of_accounts(self):
        return len(self.accounts)
