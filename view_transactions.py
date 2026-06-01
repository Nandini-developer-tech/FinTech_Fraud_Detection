from database import cursor

cursor.execute("SELECT * FROM transactions")

for row in cursor.fetchall():
    print(row)