import sqlite3
#First method
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

#second Method


# Connect to database
connection = sqlite3.connect("sql3.db")
cursor = connection.cursor()

# Get data without SQL sorting
cursor.execute("SELECT * FROM tasks")

rows = cursor.fetchall()

# Sort using Python
sorted_rows = sorted(rows, key=lambda row: row[5])

print("Sorted using Python:")

for row in sorted_rows:
    print(row)

connection.close()