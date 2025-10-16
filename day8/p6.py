import mysql.connector

# Connect to database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ajibb58xc@@",
    database="mydatabase"
)
mycursor = mydb.cursor()

# # Create table
# mycursor.execute("""
#     CREATE TABLE IF NOT EXISTS students (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         name VARCHAR(255),
#         age INT,
#         course VARCHAR(255)
#     )
# """)

# Insert data
# students = [
#     ("pratap", 24, "CS"),
#     ("pooja", 29, "Math"),
#     ("shreya", 29, "Physics")
# ]

# mycursor.executemany("INSERT INTO students (name, age, course) VALUES (%s, %s, %s)", students)
# mydb.commit()


while True:
    name =input("enter name:")
    age =int(input("enter age:"))
    course =input("enter course:") 
    mycursor.execute("INSERT INTO students (name, age, course) VALUES (%s, %s, %s)", (name, age, course))
    mydb.commit()
    ch = input("do you want to add more data (y/n):")
    if ch.lower() != 'y':
        break 
# Show data
mycursor.execute("SELECT * FROM students")
result = mycursor.fetchall()

for row in result:
    print(row)

mydb.close()
