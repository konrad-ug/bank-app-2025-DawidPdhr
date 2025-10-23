from src.account import Account

class TestTransfers:
    def test_incoming_transfer(self):
        account = Account()
        account.incoming_transfer(75.0)
        assert account.balance == 75.0

    def test_incoming_transfer_negative_amount(self):
        account = Account()
        account.incoming_transfer(-75.0)
        assert account.balance == 0.0

    def test_outgoing_transfer(self):
        account = Account()
        account.balance = 100.0
        account.outgoing_transfer(75.0)
        assert account.balance == 25.0

    def test_outgoing_transfer_negative_amount(self):
        account = Account()
        account.outgoing_transfer(-75.0)
        assert account.balance == 0.0

    def test_outgoing_transfer_exceeding_balance(self):
        account = Account()
        account.balance = 100.0
        account.outgoing_transfer(175.0)
        assert account.balance == 100.0

    