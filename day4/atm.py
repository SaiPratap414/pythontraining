#create a atm machine program using def and customer details as dictionary card pin name balance

print("***AXIS bank ATM***")
customer ={
    "card":9398169,
    "pin":1863,
    "name":"john",
    "balance": 10000
}

cardnum = input("Enter Card Number: ")
pinnumber = input("Enter pin:")
if cardnum == str(customer["card"]) and pinnumber == str(customer["pin"]):
    print(customer)
    while True:
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Balance")
        print("4.Exit")
        ch=input("enter choice:")
        if ch=="1":
            amount=int(input("enter amount: "))
            customer["balance"] += amount
            
        elif ch=="2":
            amount=int(input("enter amount to withdraw: "))
            if amount <= customer["balance"]:
                customer["balance"] -= amount
            else:
                print("Insufficient balance!")
        elif ch=="3":
            print(f"Your current balance is: {customer['balance']}")
        elif ch=="4":
            print("Thank you for using AXIS bank ATM!")
            break
        else:
            print("Invalid choice! Please try again.")
else:
    print("Invalid card number or PIN!")
            