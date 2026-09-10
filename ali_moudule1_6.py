class PersonAddress:
    def __init__(self, name, contact, address, phone):
        self.name = name
        self.contact = contact
        self.address = address
        self.phone = phone

    def save_to_file(self):
        file = open("address.txt", "a")

        file.write("Name: " + self.name + "\n")
        file.write("Contact: " + self.contact + "\n")
        file.write("Address: " + self.address + "\n")
        file.write("Phone: " + self.phone + "\n")
        file.write("--------------------\n")

        file.close()


# User input
name = input("Enter name: ")
contact = input("Enter contact: ")
address = input("Enter address: ")
phone = input("Enter phone number: ")

# Create object
person = PersonAddress(name, contact, address, phone)

# Save data
person.save_to_file()

print("Address saved successfully.")