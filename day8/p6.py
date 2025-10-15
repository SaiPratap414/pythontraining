import mysql.connector

# Connect and setup
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ajibb58xc@@",
    database="mydatabase"
)
mycursor = mydb.cursor()

# Create table
mycursor.execute("DROP TABLE IF EXISTS customers")
mycursor.execute("""
    CREATE TABLE customers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255)
    )
""")

# Insert data
customers = [
    ("John Doe", "john@email.com"),
    ("Jane Smith", "jane@email.com"),
    ("Bob Johnson", "bob@email.com")
]

mycursor.executemany("INSERT INTO customers (name, email) VALUES (%s, %s)", customers)
mydb.commit()

# Select and display
mycursor.execute("SELECT * FROM customers")
result = mycursor.fetchall()

print("Customer data:")
for row in result:
    print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

mydb.close()
