class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.__account_number = account_number
        self.__balance = balance
        self.__opening = date_of_opening
        self.__name = customer_name
        
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if self.__balance <= amount :
            print("you broke")
        else:
            self.__balance -= amount
    
    def check_balance(self):
        return self.__balance
