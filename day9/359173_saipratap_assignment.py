# Student Record Management - 359173 Sai Pratap

def add_student():
    roll_no = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    
    with open("students.txt", "a") as file:
        file.write(f"{roll_no},{name},{marks}\n")
    
    print("Record added!")

def view_records():
    try:
        with open("students.txt", "r") as file:
            print("\nAll Records:")
            for line in file:
                roll_no, name, marks = line.strip().split(",")
                print(f"Roll: {roll_no}, Name: {name}, Marks: {marks}")
    except:
        print("No records found!")

while True:
    print("\n1. Add Student")
    print("2. View Records") 
    print("3. Exit")
    
    choice = input("Choice: ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        view_records()
    elif choice == '3':
        break
    else:
        print("Invalid!")