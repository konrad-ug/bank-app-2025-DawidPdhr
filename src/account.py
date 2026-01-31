class Account:
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
