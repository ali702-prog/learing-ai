import sqlite3


def search_description(search):

    # Connect to database
    connection = sqlite3.connect("sql3.db")
    cursor = connection.cursor()

    # Search only description
    cursor.execute("""
        SELECT *
        FROM tasks
        WHERE description LIKE ?
    """, ('%' + str(search) + '%',))

    rows = cursor.fetchall()

    connection.close()

    return rows


# Ask user what to search
search = input("Enter letters or number to search: ")

results = search_description(search)

print("\nBest matching rows:")

for row in results:
    print(row)