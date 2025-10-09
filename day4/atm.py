#create a atm machine program using def and customer details as dictionary card pin name balance


def show_menu():
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Balance")
    print("4.Exit")

def deposit(customer):
    amount = int(input("Enter amount: "))
    customer["balance"] += amount
    print(f"Deposited {amount}. New balance: {customer['balance']}")

def withdraw(customer):
    amount = int(input("Enter amount to withdraw: "))
    if amount <= customer["balance"]:
        customer["balance"] -= amount
        print(f"Withdrawn {amount}. New balance: {customer['balance']}")
    else:
        print("Insufficient balance!")

def check_balance(customer):
    print(f"Your current balance is: {customer['balance']}")

def atm():
    print("***AXIS bank ATM***")
    customer = {
        "card": 9398169,
        "pin": 1863,
        "name": "john",
        "balance": 10000
    }
    cardnum = input("Enter Card Number: ")
    pinnumber = input("Enter pin:")
    if cardnum == str(customer["card"]) and pinnumber == str(customer["pin"]):
        print(f"Welcome, {customer['name']}!")
        while True:
            show_menu()
            ch = input("Enter choice: ")
            if ch == "1":
                deposit(customer)
            elif ch == "2":
                withdraw(customer)
            elif ch == "3":
                check_balance(customer)
            elif ch == "4":
                print("Thank you for using AXIS bank ATM!")
                break
            else:
                print("Invalid choice! Please try again.")
    else:
        print("Invalid card number or PIN!")

if __name__ == "__main__":
    atm()
            