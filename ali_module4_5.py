import sqlite3
import time

# Connect to database
connection = sqlite3.connect("sql3.db")
cursor = connection.cursor()

task_id = 1

# Read original value
cursor.execute(
    "SELECT title, status FROM tasks WHERE id = ?",
    (task_id,)
)

original_task = cursor.fetchone()

if original_task is None:
    print("Task not found.")
    connection.close()
    exit()


original_status = original_task[1]

print("Original value:")
print(original_task)


# Change the row
cursor.execute(
    "UPDATE tasks SET status = ? WHERE id = ?",
    ("Completed", task_id)
)

connection.commit()

print("\nChanged value:")

cursor.execute(
    "SELECT id, title, description, status, created_at FROM tasks WHERE id = ?",
    (task_id,)
)

print(cursor.fetchone())


# Wait 15 seconds
print("\nWaiting 15 seconds...")
time.sleep(15)


# Revert back
cursor.execute(
    "UPDATE tasks SET status = ? WHERE id = ?",
    (original_status, task_id)
)

connection.commit()

print("\nReverted value:")

cursor.execute(
    "SELECT id, title, description, status, created_at FROM tasks WHERE id = ?",
    (task_id,)
)

print(cursor.fetchone())


connection.close()