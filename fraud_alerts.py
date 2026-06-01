from database import cursor

cursor.execute("SELECT * FROM fraud_alerts")

for row in cursor.fetchall():
    print(row)