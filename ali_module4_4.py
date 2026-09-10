import sqlite3

# Connect to database
connection = sqlite3.connect("sql3.db")

# Create cursor
cursor = connection.cursor()

# Find all tables
cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type='table'
""")

tables = cursor.fetchall()

# Display tables
print("Database Tables:")

for table in tables:
    print(table[0])

# Close connection
connection.close()


import sqlite3

connection = sqlite3.connect("sql3.db")
cursor = connection.cursor()

cursor.execute("PRAGMA table_info(tasks)")

columns = cursor.fetchall()

print("Tasks Table Structure:")

for column in columns:
    print(column)

connection.close()