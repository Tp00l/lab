from account import *
# The test module created to test the account module for lab 12


class Test:
    def setup_method(self):
        self.account_1 = Account('John')
        self.account_2 = Account('Jessica')

    def teardown_method(self):
        del self.account_1
        del self.account_2

    def test_init(self):
        assert self.account_1.get_balance() == 0
        assert self.account_1.get_name() == 'John'
        assert self.account_2.get_balance() == 0
        assert self.account_2.get_name() == 'Jessica'

    def test_deposit(self):
        assert self.account_1.deposit(-2) is False
        assert self.account_1.get_balance() == 0
        assert self.account_1.deposit(0) is False
        assert self.account_1.get_balance() == 0
        assert self.account_1.deposit(10) is True
        assert self.account_1.get_balance() == 10
        assert self.account_2.deposit(-2.75) is False
        assert self.account_2.get_balance() == 0
        assert self.account_2.deposit(0) is False
        assert self.account_2.get_balance() == 0
        assert self.account_2.deposit(51.50) is True
        assert self.account_2.get_balance() == 51.50

    def test_withdraw(self):
        self.account_1.deposit(10)
        assert self.account_1.withdraw(-3) is False
        assert self.account_1.get_balance() == 10
        assert self.account_1.withdraw(0) is False
        assert self.account_1.get_balance() == 10
        assert self.account_1.withdraw(11) is False
        assert self.account_1.get_balance() == 10
        assert self.account_1.withdraw(5) is True
        assert self.account_1.get_balance() == 5
        self.account_2.deposit(51.50)
        assert self.account_2.withdraw(-1.50) is False
        assert self.account_2.get_balance() == 51.50
        assert self.account_2.withdraw(0) is False
        assert self.account_2.get_balance() == 51.50
        assert self.account_2.withdraw(61.50) is False
        assert self.account_2.get_balance() == 51.50
        assert self.account_2.withdraw(11.50) is True
        assert self.account_2.get_balance() == 40
