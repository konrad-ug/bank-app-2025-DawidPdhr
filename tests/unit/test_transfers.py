import pytest
from src.account import Account

class TestTransfers:
    @pytest.fixture(autouse=True)
    def account(self):
        return Account()
    
    @pytest.mark.parametrize("initial_balance, incoming_list, outgoing_list, expected_balance", [
        (0.0, [75.0], [], 75.0),
        (0.0, [-75.0], [], 0.0),
        (100.0, [], [75.0], 25.0),
        (100.0, [], [-75.0], 100.0),
        (100.0, [], [175.0], 100.0),
        (100.0, [125.0, 75.0], [50.0, 10.0, 200.0], 40.0)
    ],
    ids=[
        "casual incoming",
        "incoming with negative amount",
        "casual outgoing",
        "outgoing with negative amount",
        "outgoing exceeding balance",
        "two incoming and three outgoing"
    ])
    def test_transfer(self, account, initial_balance, incoming_list, outgoing_list, expected_balance):
        account.balance = initial_balance
        for transfer in incoming_list:
            account.incoming_transfer(transfer)
        for transfer in outgoing_list:
            account.outgoing_transfer(transfer)
        assert account.balance == expected_balance

    