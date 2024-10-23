import os

balance_file = 'balance.txt'
transactions_file = 'transactions.txt'


def load_balance():
    if os.path.exists(balance_file):
        with open(balance_file, 'r') as file:
            balance = file.read().strip()
            try:
                return float(balance)
            except ValueError:
                return 0.0
    return 0.0


def current_balance(balance):
    with open(balance_file, 'w') as file:
        file.write(str(balance))


def display_balance():
    balance = load_balance()
    print(f'Current balance: {balance:.2f}.')


def log_transaction(transaction_type, amount):
    with open(transactions_file, 'a') as file:
        file.write(f"{transaction_type}: {amount:.2f}\n")


def expenses_income():
    print('Choose transaction')
    print('1. Replenishment')
    print('2. Withdrawal')
    print('Your choice: ')

    try:
        choice = int(input())
        amount = float(input('Enter sum: '))

        balance = load_balance()

        if choice == 1:
            balance += amount
            current_balance(balance)
            log_transaction('Replenishment', amount)
            print('Your balance has been replenished')

        elif choice == 2:
            if balance >= amount:
                balance -= amount
                current_balance(balance)
                log_transaction('Withdrawal money', amount)
                print('Money has been withdrawn from the account')
            else:
                print('Insufficient funds')
        else:
            print('Wrong transaction')
    except ValueError:
        print("Error: Please enter a numeric value to select the operation.")


def transaction_history():
    if os.path.exists(transactions_file):
        with open(transactions_file, 'r') as file:
            transactions = file.readlines()
        print('Transaction history:')
        if transactions:
            for transaction in transactions:
                print(transaction.strip())
        else:
            print('Transaction history is empty')
    else:
        print('Transaction history is empty')


def main():
    while True:
        print("\nChoose operation")
        print("1. Display current balance")
        print("2. Enter new transaction")
        print("3. Display transaction history")
        print("4. Exit")

        try:
            choose = int(input())

            if choose == 1:
                display_balance()

            elif choose == 2:
                expenses_income()

            elif choose == 3:
                transaction_history()

            elif choose == 4:
                print("Completing the calculator")
                break

            else:
                print("Wrong operation")
        except ValueError:
            print("Error: Please enter a numeric value to select the operation.")


main()
