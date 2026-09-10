import sqlite3


# Connect to database
connection = sqlite3.connect("sql3.db")

# Create cursor
cursor = connection.cursor()


# Create tasks table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")


# Save changes
connection.commit()

# Close database
connection.close()


print("Database and tasks table created successfully.")