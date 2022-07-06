from locale import currency


class Atm:
    def __init__(self):
        print("Hello World")
        self.pin = ""
        self.balance = 0

        self.menu()

    def menu(self):
        user_input = input(""" 

                        Hello, How would you like to proceed?
                        1. Enter 1 to Create Pin ?
                        2. Enter 2 to Check Balance ?
                        3. Enter 3 to Withdraw ?
                        4. Enter 4 to Deposit ?
                        5. Enter 5 to Exit ?

        """)

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.check_balance()
        elif user_input == "3":
            self.withdraw_amount()
        elif user_input == "4":
            self.deposit_amount()
        else:
            print("Thank you for Banking with us")

    def create_pin(self):
        self.pin = input("Enter pin : ")
        print("Pin Set Successfully")

    def withdraw_amount(self):
        temp = input("Enter Pin")
        if temp == self.pin:
            amount = int(input("Enter the Amount : "))
            if amount < self.balance:
                self.balance = self.balance - amount
                print("Withdrawl SuccessFul")
            else:
                print("Operation Failed")
        else:
            print("Invalid Pin")

    def deposit_amount(self):
        temp = input("Enter Pin")
        if temp == self.pin:
            amount = int(input("Enter the amount : "))
            self.balance = self.balance + amount
            print("Deposit SuccessFul")
        else:
            print("Invalid Pin")

    def check_balance(self):
        temp = input("Enter Pin")
        if temp == self.pin:
            current_balance = self.balance
            print("Saving Balance :",current_balance)
        else:
            print("Invalid Pin")

sbi = Atm()
print(sbi)