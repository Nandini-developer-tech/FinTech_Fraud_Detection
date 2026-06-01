from database import conn, cursor

customer_id = int(input("Customer ID: "))
balance = float(input("Initial Balance: "))

query = """
INSERT INTO accounts(customer_id,balance)
VALUES(%s,%s)
"""

cursor.execute(query,(customer_id,balance))
conn.commit()