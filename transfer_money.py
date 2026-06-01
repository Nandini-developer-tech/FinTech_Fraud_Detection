from database import conn, cursor

sender = int(input("Sender ID: "))
receiver = int(input("Receiver ID: "))
amount = float(input("Amount: "))

# Insert transaction
query = """
INSERT INTO transactions
(sender_id, receiver_id, amount, status)
VALUES (%s, %s, %s, %s)
"""

cursor.execute(query, (sender, receiver, amount, "SUCCESS"))
conn.commit()

transaction_id = cursor.lastrowid

# Fraud detection
if amount > 50000:
    fraud_query = """
    INSERT INTO fraud_alerts(transaction_id, reason)
    VALUES (%s, %s)
    """

    cursor.execute(
        fraud_query,
        (transaction_id, "High Amount Transaction")
    )
    conn.commit()

    print("Fraud Alert Recorded!")