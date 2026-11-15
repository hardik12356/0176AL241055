class ATM:
    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    def check_balance(self, pin):
        if pin == self.__pin:
            print("Balance:", self.__balance)
        else:
            print("Incorrect PIN")

    def withdraw(self, pin, amount):
        if pin == self.__pin:
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawal Successful")
                print("Remaining Balance:", self.__balance)
            else:
                print("Insufficient Balance")
        else:
            print("Incorrect PIN")

obj = ATM(1234, 10000)

pin = int(input("Enter PIN: "))
obj.check_balance(pin)

amount = int(input("Enter withdrawal amount: "))
obj.withdraw(pin, amount)