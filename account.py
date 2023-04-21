class Account:
    def __init__(self, name: str) -> None:
        """
        A function to set up an account object.
        :param name: Account owner's name.
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        A method to add an amount of money to the account.
        :param amount: The amount to add to the balance.
        :return: False if the deposit fails or True if it succeeds.
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        """
        A method to take out an amount of money from the account.
        :param amount: The amount to take out of the account.
        :return: False if the withdrawal fails or True if it succeeds.
        """
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        A method to acquire the balance of the account.
        :return: The current account balance.
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        A method to acquire the name of the account owner.
        :return: The current account owner's name.
        """
        return self.__account_name
