import random as r
n = r.randint(1,100)
attempt=0
while True:
    num = int(input("enter a number"))
    attempt += 1
    if num == n:
        print(f"Congratulations! You guessed the number in {attempt} attempts.")
        break
    elif num < n:
        print("Too low, try again.")
    else:
        print("Too high, try again.")