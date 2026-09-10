import json
import random


# Create the class
class Person:
    def __init__(self, name, number, location, job_title):
        self.name = name
        self.number = number
        self.location = location
        self.job_title = job_title


# Function to create 5 random people
def create_people():

    names = ["Ali", "Ahmed", "Sara", "Mariam", "Zayed"]
    locations = ["Dubai", "Sharjah", "Abu Dhabi", "Ajman", "Fujairah"]
    jobs = ["Manager", "Teacher", "Developer", "Engineer", "Accountant"]

    people = []

    for i in range(5):

        person = Person(
            random.choice(names),
            random.randint(1000, 9999),
            random.choice(locations),
            random.choice(jobs)
        )

        people.append(person.__dict__)

    # Create JSON file
    with open("people.json", "w") as file:
        json.dump(people, file, indent=3)

    print("people.json created successfully")


# Run the function
create_people()