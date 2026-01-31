import pytest
from src.company_account import CompanyAccount
from src.personal_account import PersonalAccount


class TestCompanyTransfersHistory:
    @pytest.fixture(autouse=True)
    def account(self, mocker):
        mocker.patch(
            "src.company_account.CompanyAccount.does_nip_exist", return_value=True
        )
        return CompanyAccount("Amuse Incorporated", "1234567890")

    @pytest.mark.parametrize(
        "initial_balance, incoming_list, outgoing_list, outgoing_express_list, expected_history",
        [
            (0.0, [], [], [], []),
            (100.0, [], [], [75.0], [-75.0, -5.0]),
            (100.0, [], [], [-75.0], []),
            (100.0, [], [], [175.0], []),
            (100.0, [], [], [100.0], [-100.0, -5.0]),
            (0.0, [75.0], [], [], [75.0]),
            (0.0, [-75.0], [], [], []),
            (100.0, [], [75.0], [], [-75.0]),
            (100.0, [], [-75.0], [], []),
            (100.0, [], [175.0], [], []),
            (0.0, [500.0], [100.0], [300.0], [500.0, -100.0, -300.0, -5.0]),
        ],
        ids=[
            "fresh",
            "outgoing express transfer",
            "outgoing express transfer with negative amount",
            "outgoing express transfer exceeding balance",
            "outgoing express transfer exceeding balance by fee",
            "incoming transfer",
            "incoming transfer with negative amount",
            "outgoing transfer",
            "outgoing transfer with negative amount",
            "outgoing transfer exceeding balance",
            "incoming, outgoing and express outgoing transfers",
        ],
    )
    def test_company_history(
        self,
        account,
        initial_balance,
        incoming_list,
        outgoing_list,
        outgoing_express_list,
        expected_history,
    ):
        account.balance = initial_balance
        for transfer in incoming_list:
            account.incoming_transfer(transfer)

        for transfer in outgoing_list:
            account.outgoing_transfer(transfer)

        for transfer in outgoing_express_list:
            account.outgoing_express_transfer(transfer)
        assert account.history == expected_history


class TestPersonalTransfersHistory:
    @pytest.fixture(autouse=True)
    def account(self):
        return PersonalAccount("John", "Doe", "12345678910")

    @pytest.mark.parametrize(
        "initial_balance, incoming_list, outgoing_list, outgoing_express_list, expected_history",
        [
            (0.0, [], [], [], []),
            (100.0, [], [], [75.0], [-75.0, -1.0]),
            (100.0, [], [], [-75.0], []),
            (100.0, [], [], [175.0], []),
            (100.0, [], [], [100.0], [-100.0, -1.0]),
            (0.0, [75.0], [], [], [75.0]),
            (0.0, [-75.0], [], [], []),
            (100.0, [], [75.0], [], [-75.0]),
            (100.0, [], [-75.0], [], []),
            (100.0, [], [175.0], [], []),
            (0.0, [500.0], [100.0], [300.0], [500.0, -100.0, -300.0, -1.0]),
        ],
        ids=[
            "fresh",
            "outgoing express transfer",
            "outgoing express transfer with negative amount",
            "outgoing express transfer exceeding balance",
            "outgoing express transfer exceeding balance by fee",
            "incoming transfer",
            "incoming transfer with negative amount",
            "outgoing transfer",
            "outgoing transfer with negative amount",
            "outgoing transfer exceeding balance",
            "incoming, outgoing and express outgoing transfers",
        ],
    )
    def test_personal_history(
        self,
        account,
        initial_balance,
        incoming_list,
        outgoing_list,
        outgoing_express_list,
        expected_history,
    ):
        account.balance = initial_balance
        for transfer in incoming_list:
            account.incoming_transfer(transfer)

        for transfer in outgoing_list:
            account.outgoing_transfer(transfer)

        for transfer in outgoing_express_list:
            account.outgoing_express_transfer(transfer)
        assert account.history == expected_history
