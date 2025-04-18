import pandas as pd, re, os

class ContactManager:
    def __init__(self, filename='contacts.csv'):
        self.filename = filename
        self.contacts = []
        self.load_contacts()

    def display_contacts(self):
        print(pd.DataFrame(self.contacts))

    def load_contacts(self):
        if os.path.exists(self.filename):
            self.contacts = pd.read_csv(self.filename).to_dict(orient='records')
        else:
            self.contacts = []

    def save_contacts(self):
        df = pd.DataFrame(self.contacts)
        df.to_csv(self.filename, index=False)
    
    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")   
        email = input("Enter email: ")

        if not re.fullmatch(r'\d{10}$', phone):
            print("Invalid phone number. Must be 10 digits.")
            return
        if not re.fullmatch(r'[^@]+@[^@]+\.[^@]+', email):
            print("Invalid email format.")
            return
        
        for contact in self.contacts:
            if contact["Phone"] == phone:
                print("Contact already exists.")
                return

        contact = {
            'Contact_Id': len(self.contacts) + 1,
            'Name': name,
            'Phone': phone,
            'Email': email
        }

        self.contacts.append(contact)
        self.save_contacts()
        print("Contact added successfully.")

    def search_contact(self):
        name = input("Enter name to search: ")
        if not name:
            print("Name field cannot be empty.")
            return
        for contact in self.contacts:
            if contact["Name"].lower() == name.lower():
                print(f"Contact found: {contact}")
                return
        print("Contact not found.")

    def delete_contact(self):
        name = input("Enter name to delete: ")

        for i, contact in enumerate(self.contacts):
            if contact["Name"].lower() == name.lower():
                confirm = input(f"Are you sure you want to delete {contact['Name']}? (yes/no): ")
                if confirm.lower() == 'yes':
                    del self.contacts[i]
                    self.save_contacts()
                    print("Contact deleted successfully.")
                    return

        print("Contact not found.")

if __name__ == "__main__":
    manager = ContactManager()

    while True:
        print("\n***************************Contact Manager***************************")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Display All Contacts")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            manager.add_contact()
        elif choice == '2':
            manager.search_contact()
        elif choice == '3':
            manager.delete_contact()
        elif choice == '4':
            manager.display_contacts()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")