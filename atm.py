class ATM:
    def __init__(self):
        self.balance = 0
        self.transaction_history = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Deposit amount must be positive.')
        
        self.balance += amount
        self.transaction_history.append(f'Deposited: ${amount}')

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Withdrawal amount must be positive.')
        if amount > self.balance:
            raise ValueError('Insufficient funds.')

        self.balance -= amount
        self.transaction_history.append(f'Withdrew: ${amount}')

    def get_transaction_history(self):
        return self.transaction_history


class ATMController:
    def __init__(self):
        self.atm = ATM()

    def get_number(self, prompt):
        while True:
            try:
                number = float(input(prompt))
                return number
            except ValueError:
                print('Please enter a valid number.')

    def display_menu(self):
        print('\nWelcome to the ATM!')
        print('1. Check Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Show Transaction History')
        print('5. Exit')    

    def check_balance(self):
        balance = self.atm.check_balance()
        print(f'Your current balance is: ${balance:.2f}')    

    def deposit(self):
        while True:
            try:
                amount = self.get_number('Enter the amount to deposit: ')
                self.atm.deposit(amount)
                print(f'Successfully deposited ${amount:.2f}.')
                break
            except ValueError as error:
                print(error)    

    def withdraw(self):
        while True:
            try:
                amount = self.get_number('Enter the amount to withdraw: ')
                self.atm.withdraw(amount)
                print(f'Successfully withdrew ${amount:.2f}.')
                break
            except ValueError as error:
                print(error)    

    def show_transaction_history(self):
        history = self.atm.get_transaction_history()
        if not history:
            print("No transactions found.")
        else:
            print("Transaction History:")
            for transaction in history:
                print(transaction)

    def run(self):
        while True: 
            self.display_menu()

            choice = input('Please choose an option: ').strip().lower()  # Normalize input
            if choice in ['1', 'check balance']:
                self.check_balance()
            elif choice in ['2', 'deposit']:
                self.deposit()
            elif choice in ['3', 'withdraw']:
                self.withdraw()
            elif choice in ['4', 'show transaction history']:
                self.show_transaction_history()
            elif choice in ['5', 'exit']:
                print('Thank you for using the ATM.')
                break
            else:
                print('Invalid choice. Please try again.')


def main():
    atm = ATMController()
    atm.run()


if __name__ == '__main__':
    main()
