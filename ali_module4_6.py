import sqlite3
import random
import string

# Connect to existing database
connection = sqlite3.connect("sql3.db")
cursor = connection.cursor()

# Add new field to tasks table
try:
    cursor.execute("""
        ALTER TABLE tasks
        ADD COLUMN missing_field TEXT
    """)
    print("missing_field added successfully.")

except sqlite3.OperationalError:
    print("missing_field already exists.")


# Get all tasks
cursor.execute("SELECT id FROM tasks")
tasks = cursor.fetchall()


# Add one random character to each task
for task in tasks:
    random_character = random.choice(string.ascii_letters)

    cursor.execute(
        "UPDATE tasks SET missing_field = ? WHERE id = ?",
        (random_character, task[0])
    )


# Save changes
connection.commit()


# Display results
cursor.execute("""
    SELECT id, title, description, status, created_at, missing_field
    FROM tasks
""")

rows = cursor.fetchall()

print("\nTasks after adding missing_field:")

for row in rows:
    print(row)


# Close database
connection.close()