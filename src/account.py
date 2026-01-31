from src.smtp.smtp import SMTPClient
import datetime


class Account:
    history_email_prefix: str = ""

    def __init__(self):
        self.balance = 0.0
        self.history = []

    def incoming_transfer(self, amount):
        if isinstance(amount, float) and amount >= 0.0:
            self.balance += amount
            self.history.append(amount)
            return True
        return False

    def outgoing_transfer(self, amount):
        if isinstance(amount, float) and amount >= 0.0 and amount <= self.balance:
            self.balance -= amount
            self.history.append(-1 * amount)
            return True
        return False

    def outgoing_express_transfer(self, fee, amount):
        if isinstance(amount, float) and amount >= 0.0 and amount <= self.balance:
            self.balance -= amount + fee
            self.history.extend([-1 * amount, -1 * fee])
            return True
        return False

    def send_history_via_email(self, email_address: str) -> bool:
        smtp = SMTPClient()

        subject = (
            f'Account Transfer History {datetime.date.today().strftime("%Y-%m-%d")}'
        )

        text = f"{self.history_email_prefix} {self.history}"

        return smtp.send(subject, text, email_address)
