from database import conn, cursor

name = input("Enter Customer Name: ")

query = "INSERT INTO customers(customer_name) VALUES(%s)"
cursor.execute(query, (name,))
conn.commit()

print("Customer Added Successfully")