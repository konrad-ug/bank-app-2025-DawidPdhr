from src.personal_account import PersonalAccount

class TestPersonalLoans:
    def test_personal_loan_three_incoming_transfers(self):
        account = PersonalAccount("John", "Doe", "12345678910")
        account.history = [200.0, 300.0, 100.0]
        result = account.submit_for_loan(1000.0)
        assert result
        assert account.balance == 1000.0

    def test_personal_loan_sum_of_five_transactions(self):
        account = PersonalAccount("John", "Doe", "12345678910")
        account.history = [200.0, 300.0, 100.0, -150.0, -50.0]
        result = account.submit_for_loan(300.0)
        assert result
        assert account.balance == 300.0

    def test_personal_loan_three_transactions_not_all_incoming(self):
        account = PersonalAccount("John", "Doe", "12345678910")
        account.history = [200.0, -300.0, 100.0]
        result = account.submit_for_loan(1000.0)
        assert not result
        assert account.balance == 0.0

    def test_personal_loan_sum_of_five_transactions_less_than_loan(self):
        account = PersonalAccount("John", "Doe", "12345678910")
        account.history = [200.0, 300.0, 100.0, -150.0, -50.0]
        result = account.submit_for_loan(500.0)
        assert not result
        assert account.balance == 0.0

    def test_personal_loan_last_three_of_five_transactions_incoming(self):
        account = PersonalAccount("John", "Doe", "12345678910")
        account.history = [-200.0, -300.0, 100.0, 150.0, 50.0]
        result = account.submit_for_loan(750.0)
        assert result
        assert account.balance == 750.0
    
    def test_personal_loan_negative(self):
        account = PersonalAccount("John", "Doe", "12345678910")
        account.history = [200.0, 300.0, 100.0]
        result = account.submit_for_loan(-300.0)
        assert not result
        assert account.balance == 0.0
    
    def test_personal_loan_not_number(self):
        account = PersonalAccount("John", "Doe", "12345678910")
        account.history = [200.0, 300.0, 100.0]
        result = account.submit_for_loan(True)
        assert not result
        assert account.balance == 0.0
    
    def test_personal_loan_two_transactions(self):
        account = PersonalAccount("John", "Doe", "12345678910")
        account.history = [200.0, 300.0]
        result = account.submit_for_loan(250.0)
        assert not result
        assert account.balance == 0.0
    
    def test_personal_loan_four_transactions_success(self):
        account = PersonalAccount("John", "Doe", "12345678910")
        account.history = [-200.0, 300.0, 150.0, 200.0]
        result = account.submit_for_loan(250.0)
        assert result
        assert account.balance == 250.0
    
    def test_personal_loan_four_transactions_fail(self):
        account = PersonalAccount("John", "Doe", "12345678910")
        account.history = [-200.0, 300.0, -150.0, 200.0]
        result = account.submit_for_loan(250.0)
        assert not result
        assert account.balance == 0.0
    
