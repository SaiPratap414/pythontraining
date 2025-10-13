# Simple Banking System
customers = {}  # Dictionary to store all customer data

def new_customer():
    """Create a new customer account"""
    print("\n=== New Customer ===")
    
    account_num = input("Enter Account#: ")
    
    # Check if account already exists
    if account_num in customers:
        print("Account already exists!")
        return
    
    pin = input("Enter Pin#: ")
    confirm_pin = input("Confirm Pin#: ")
    
    # Check if PINs match
    if pin != confirm_pin:
        print("PINs do not match!")
        return
    
    name = input("Enter Name: ")
    
    # Create new account
    customers[account_num] = {
        'pin': pin,
        'name': name,
        'balance': 0
    }
    
    print("Congratulations! Your account has been created.")

def existing_customer():
    """Handle existing customer operations"""
    print("\n=== Existing Customer ===")
    
    account_num = input("Enter Account#: ")
    
    # Check if account exists
    if account_num not in customers:
        print("Account not found!")
        return
    
    pin = input("Enter Pin#: ")
    
    # Check PIN
    if customers[account_num]['pin'] != pin:
        print("Wrong PIN!")
        return
    
    name = customers[account_num]['name']
    print(f"Welcome {name}!")
    
    # Show customer menu
    while True:
        print(f"\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Enter Choice: ")
        
        if choice == '1':
            balance = customers[account_num]['balance']
            print(f"Balance: ${balance}")
            
        elif choice == '2':
            amount = float(input("Enter amount: $"))
            customers[account_num]['balance'] += amount
            print(f"Deposited ${amount}")
            print(f"New Balance: ${customers[account_num]['balance']}")
            
        elif choice == '3':
            amount = float(input("Enter amount: $"))
            if amount > customers[account_num]['balance']:
                print("Not enough money!")
            else:
                customers[account_num]['balance'] -= amount
                print(f"Withdrew ${amount}")
                print(f"New Balance: ${customers[account_num]['balance']}")
                
        elif choice == '4':
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

def main():
    """Main program"""
    while True:
        print("\n*** My Bank ***")
        print("1. New Customer")
        print("2. Existing Customer")
        print("3. Exit")
        
        choice = input("Enter Choice: ")
        
        if choice == '1':
            new_customer()
            
        elif choice == '2':
            existing_customer()
            
        elif choice == '3':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice!")
        
        # Ask to continue
        continue_choice = input("Continue?(y/n): ")
        if continue_choice.lower() != 'y':
            print("Goodbye!")
            break

# Start the program
if __name__ == "__main__":
    main()