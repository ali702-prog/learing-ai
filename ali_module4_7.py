import sqlite3

# Connect to database
connection = sqlite3.connect("sql3.db")
cursor = connection.cursor()

# Sort using SQL
cursor.execute("""
    SELECT * FROM tasks
    ORDER BY missing_field ASC
""")

rows = cursor.fetchall()

print("Sorted using SQL:")

for row in rows:
    print(row)

connection.close()