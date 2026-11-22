# Banking System using Object-Oriented Programming

# 1. Base Class
class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.__balance = balance  # Private attribute

    # Deposit money
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero!")
            return

        self.__balance += amount
        print(f"Rs. {amount:.2f} deposited successfully.")
        print(f"Updated Balance: Rs. {self.__balance:.2f}")

    # Withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero!")
            return False

        if amount > self.__balance:
            print("Insufficient balance!")
            return False

        self.__balance -= amount
        print(f"Rs. {amount:.2f} withdrawn successfully.")
        print(f"Updated Balance: Rs. {self.__balance:.2f}")
        return True

    # Protected interface for derived classes
    def deduct_balance(self, amount):
        if amount <= 0 or amount > self.__balance:
            return False

        self.__balance -= amount
        return True

    # Access private balance safely
    def get_balance(self):
        return self.__balance

    # Display account details
    def display_details(self):
        print("\n----- ACCOUNT DETAILS -----")
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print(f"Balance: Rs. {self.get_balance():.2f}")


# 2. Derived Class: Savings Account
class SavingsAccount(BankAccount):
    def __init__( self, account_holder, account_number, balance=0, interest_rate=4.0, minimum_balance=1000 ):
        super().__init__(account_holder, account_number, balance)
        self.interest_rate = interest_rate
        self.minimum_balance = minimum_balance

    # Method overriding
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero!")
            return False

        if self.get_balance() - amount < self.minimum_balance:
            print("Transaction denied! Minimum balance must be maintained.")
            return False

        return super().withdraw(amount)

    # Calculate annual interest
    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        print(f"Annual Interest: Rs. {interest:.2f}")
        return interest

    # Method overriding
    def display_details(self):
        super().display_details()
        print("Account Type: Savings Account")
        print(f"Interest Rate: {self.interest_rate}%")
        print(f"Minimum Balance: Rs. {self.minimum_balance:.2f}")


# 3. Derived Class: Current Account
class CurrentAccount(BankAccount):
    def __init__(
        self,
        account_holder,
        account_number,
        balance=0,
        overdraft_limit=5000
    ):
        super().__init__(account_holder, account_number, balance)
        self.overdraft_limit = overdraft_limit

    # Method overriding with overdraft support
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero!")
            return False

        current_balance = self.get_balance()

        if amount > current_balance + self.overdraft_limit:
            print("Transaction denied! Overdraft limit exceeded.")
            return False

        # Withdraw available balance through the parent method
        if amount <= current_balance:
            return super().withdraw(amount)

        # Withdraw the available balance first
        if current_balance > 0:
            if not super().withdraw(current_balance):
                return False

        # Deduct the remaining amount through the base-class interface
        remaining = amount - current_balance

        if self.deduct_balance(remaining):
            print(f"Rs. {amount:.2f} withdrawn successfully using overdraft.")
            print(f"Updated Balance: Rs. {self.get_balance():.2f}")
            return True

        print("Transaction failed!")
        return False

    # Method overriding
    def display_details(self):
        super().display_details()
        print("Account Type: Current Account")
        print(f"Overdraft Limit: Rs. {self.overdraft_limit:.2f}")


# 4. Polymorphism
def perform_transaction(account):
    print("\n----- POLYMORPHIC TRANSACTION -----")
    account.display_details()
    account.withdraw(500)


# 5. Main Program
def main():
    accounts = {}

    while True:
        print("\n========== BANK MANAGEMENT SYSTEM ==========")
        print("1. Create Savings Account")
        print("2. Create Current Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Check Balance")
        print("6. Display Account Details")
        print("7. Calculate Savings Interest")
        print("8. Demonstrate Polymorphism")
        print("9. Exit")

        choice = input("Enter your choice: ").strip()

        if choice in ("1", "2"):
            holder = input("Enter account holder name: ").strip()
            number = input("Enter account number: ").strip()

            if not holder or not number:
                print("Name and account number cannot be empty!")
                continue

            if number in accounts:
                print("Account number already exists!")
                continue

            try:
                balance = float(input("Enter initial balance: Rs. "))

                if balance < 0:
                    print("Initial balance cannot be negative!")
                    continue

                if choice == "1":
                    rate = float(
                        input("Enter annual interest rate (%): ")
                    )
                    minimum = float(
                        input("Enter minimum balance: Rs. ")
                    )

                    if rate < 0 or minimum < 0:
                        print(
                            "Interest rate and minimum balance "
                            "cannot be negative!"
                        )
                        continue

                    if balance < minimum:
                        print(
                            "Initial balance must meet the "
                            "minimum balance requirement!"
                        )
                        continue

                    accounts[number] = SavingsAccount(
                        holder, number, balance, rate, minimum
                    )

                else:
                    overdraft = float(
                        input("Enter overdraft limit: Rs. ")
                    )

                    if overdraft < 0:
                        print("Overdraft limit cannot be negative!")
                        continue

                    accounts[number] = CurrentAccount(
                        holder, number, balance, overdraft
                    )

                print("Account created successfully!")

            except ValueError:
                print("Invalid input! Please enter numeric values.")

        elif choice in ("3", "4", "5", "6", "7", "8"):
            number = input("Enter account number: ").strip()
            account = accounts.get(number)

            if account is None:
                print("Account not found!")
                continue

            if choice == "3":
                try:
                    amount = float(
                        input("Enter deposit amount: Rs. ")
                    )
                    account.deposit(amount)
                except ValueError:
                    print("Please enter a valid amount!")

            elif choice == "4":
                try:
                    amount = float(
                        input("Enter withdrawal amount: Rs. ")
                    )
                    account.withdraw(amount)
                except ValueError:
                    print("Please enter a valid amount!")

            elif choice == "5":
                print(
                    f"Current Balance: Rs. "
                    f"{account.get_balance():.2f}"
                )

            elif choice == "6":
                account.display_details()

            elif choice == "7":
                if isinstance(account, SavingsAccount):
                    account.calculate_interest()
                else:
                    print(
                        "Interest calculation is available "
                        "for savings accounts only."
                    )

            elif choice == "8":
                perform_transaction(account)

        elif choice == "9":
            print(
                "Thank you for using the Bank Management System!"
            )
            break

        else:
            print("Invalid choice! Please select 1-9.")


if __name__ == "__main__":
    main()
