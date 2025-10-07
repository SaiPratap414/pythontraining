username = input("Enter a username: ")

# Check if length is between 5 and 15 characters
if 5 <= len(username) <= 15:
    # Check if username contains only alphabets and numbers
    if username.isalnum():
        print("Valid username!")
    else:
        print("Invalid! Username should contain only alphabets and numbers.")
else:
    print("Invalid! Username length should be between 5 and 15 characters.")