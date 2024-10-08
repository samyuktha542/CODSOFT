import json

class Contact:
    def __init__(self, name, phone, email, address=None, birthday=None, notes=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.birthday = birthday
        self.notes = notes

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
            "birthday": self.birthday,
            "notes": self.notes,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            phone=data["phone"],
            email=data["email"],
            address=data.get("address"),
            birthday=data.get("birthday"),
            notes=data.get("notes"),
        )

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        self.contacts[contact.name] = contact
        print(f"Contact {contact.name} added.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        for contact in self.contacts.values():
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, "
                  f"Address: {contact.address}, Birthday: {contact.birthday}, Notes: {contact.notes}")

    def update_contact(self, name, **kwargs):
        if name in self.contacts:
            contact = self.contacts[name]
            for key, value in kwargs.items():
                if value is not None:
                    setattr(contact, key, value)
            print(f"Contact {name} updated.")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted.")
        else:
            print(f"Contact {name} not found.")

    def save_contacts(self, filename):
        with open(filename, 'w') as file:
            json.dump([contact.to_dict() for contact in self.contacts.values()], file)
        print(f"Contacts saved to {filename}.")

    def load_contacts(self, filename):
        try:
            with open(filename, 'r') as file:
                contacts_data = json.load(file)
                for contact_data in contacts_data:
                    contact = Contact.from_dict(contact_data)
                    self.add_contact(contact)
            print(f"Contacts loaded from {filename}.")
        except FileNotFoundError:
            print(f"No contacts file found at {filename}.")
        except json.JSONDecodeError:
            print("Error reading the contacts file.")

def main():
    contact_book = ContactBook()
    contact_book.load_contacts('contacts.json')

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Save Contacts")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address (optional): ")
            birthday = input("Enter birthday (optional): ")
            notes = input("Enter notes (optional): ")
            contact = Contact(name, phone, email, address, birthday, notes)
            contact_book.add_contact(contact)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            name = input("Enter name of the contact to update: ")
            phone = input("Enter new phone (leave blank to skip): ") or None
            email = input("Enter new email (leave blank to skip): ") or None
            address = input("Enter new address (leave blank to skip): ") or None
            birthday = input("Enter new birthday (leave blank to skip): ") or None
            notes = input("Enter new notes (leave blank to skip): ") or None
            contact_book.update_contact(name, phone=phone, email=email, address=address, birthday=birthday, notes=notes)

        elif choice == '4':
            name = input("Enter name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '5':
            contact_book.save_contacts('contacts.json')

        elif choice == '6':
            print("Exiting contact book.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
