import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="fintech_db"
)

cursor = conn.cursor()