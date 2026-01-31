from src.company_account import CompanyAccount
from src.personal_account import PersonalAccount
from src.smtp.smtp import SMTPClient
import pytest


class TestSendHistoryEmail:
    @pytest.fixture()
    def personal_account(self):
        personal_account = PersonalAccount("John", "Doe", "12345678910")
        return personal_account

    @pytest.fixture()
    def company_account(self, mocker):
        mock_verify_nip_api = mocker.Mock()
        mock_verify_nip_api.does_nip_exist.return_value = True
        mocker.patch.object(
            CompanyAccount, "does_nip_exist", new_callable=mock_verify_nip_api
        )

        company_account = CompanyAccount("Amuse Incorporated", "1234567890")
        return company_account

    @pytest.mark.parametrize(
        "history, wasSent, email_address",
        [
            ([100, -1, 500], True, "test@test"),
            ([100, -1, 500], False, "test@test"),
            ([], True, "test@test"),
        ],
        ids=[
            "Sent succesfully",
            "Failed to send",
            "Empty history",
        ],
    )
    def test_personal_transfer_history_email(
        self, mocker, personal_account, history, wasSent, email_address
    ):
        mock_send = mocker.patch("src.smtp.smtp.SMTPClient.send", return_value=wasSent)
        personal_account.history = history

        result = personal_account.send_history_via_email(email_address)

        assert result is wasSent
        mock_send.assert_called_once()
        # check those parameters in debug mock_send.call_args.args
        (subject, text, email), _ = mock_send.call_args

    @pytest.mark.parametrize(
        "history, wasSent, email_address",
        [
            ([5000, -1000, 500], True, "test@test"),
            ([5000, -1000, 500], False, "test@test"),
            ([], True, "test@test"),
        ],
        ids=[
            "Sent succesfully",
            "Failed to send",
            "Empty history",
        ],
    )
    def test_company_transfer_history_email(
        self, mocker, company_account, history, wasSent, email_address
    ):
        mock_send = mocker.patch("src.smtp.smtp.SMTPClient.send", return_value=wasSent)
        company_account.history = history

        result = company_account.send_history_via_email(email_address)

        assert result is wasSent
        mock_send.assert_called_once()
        # check those parameters in debug mock_send.call_args.args
        (subject, text, email), _ = mock_send.call_args
