import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="salesdb"
)

cursor = mydb.cursor()
cursor.execute("SELECT * FROM orders")
rows = cursor.fetchall()

with open("orders.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([i[0] for i in cursor.description])  # column names
    writer.writerows(rows)

print("orders.csv exported")
