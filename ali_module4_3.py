from fastapi import FastAPI
import sqlite3

app = FastAPI()


@app.post("/tasks")
def add_tasks():

    # Connect to database
    connection = sqlite3.connect("sql3.db")
    cursor = connection.cursor()

    # Add first task
    cursor.execute("""
        INSERT INTO tasks (title, description, status)
        VALUES (?, ?, ?)
    """, ("Learn SQL", "Practice SQLite database", "Pending"))

    # Add second task
    cursor.execute("""
        INSERT INTO tasks (title, description, status)
        VALUES (?, ?, ?)
    """, ("Learn FastAPI", "Practice POST API", "In Progress"))

    # Save changes
    connection.commit()

    # Close database
    connection.close()

    return {
        "message": "2 tasks added successfully"
    }