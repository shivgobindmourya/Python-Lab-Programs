# Program: Dictionary-Based Contact Management System

# Store contacts in a dictionary
contacts = {
    "Shiv": {"Phone": "9876543210", "Email": "shiv@example.com"},
    "Rahul": {"Phone": "8765432109", "Email": "rahul@example.com"},
    "Aman": {"Phone": "7654321098", "Email": "aman@example.com"}
}


# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ").strip()

    if not name:
        print("Contact name cannot be empty.")
        return

    if name in contacts:
        print("Contact already exists!")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    contacts[name] = {"Phone": phone, "Email": email}
    print("Contact added successfully!")


# Function to display all contacts
def display_contacts():
    if not contacts:
        print("No contacts available.")
        return

    print("\n========== ALL CONTACTS ==========")

    for name, details in contacts.items():
        print(f"Name  : {name}")
        print(f"Phone : {details['Phone']}")
        print(f"Email : {details['Email']}")
        print("-" * 35)


# Function to search for a contact
def search_contact():
    name = input("Enter name to search: ").strip()

    # List comprehension for dynamic lookup
    results = [
        (contact_name, details)
        for contact_name, details in contacts.items()
        if name.lower() in contact_name.lower()
    ]

    if results:
        print("\n========== SEARCH RESULTS ==========")

        for contact_name, details in results:
            print(f"Name  : {contact_name}")
            print(f"Phone : {details['Phone']}")
            print(f"Email : {details['Email']}")
    else:
        print("Contact not found.")


# Function to update a contact
def update_contact():
    name = input("Enter contact name to update: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    print("1. Update Phone")
    print("2. Update Email")
    print("3. Update Both")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        contacts[name]["Phone"] = input("Enter new phone number: ").strip()
        print("Phone number updated successfully!")

    elif choice == "2":
        contacts[name]["Email"] = input("Enter new email address: ").strip()
        print("Email updated successfully!")

    elif choice == "3":
        contacts[name]["Phone"] = input("Enter new phone number: ").strip()
        contacts[name]["Email"] = input("Enter new email address: ").strip()
        print("Contact updated successfully!")

    else:
        print("Invalid choice.")


# Function to delete a contact
def delete_contact():
    name = input("Enter contact name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


# Function to demonstrate dictionary methods
def dictionary_methods():
    print("\n========== DICTIONARY METHODS ==========")

    print("Contact Names (.keys()):")
    print(list(contacts.keys()))

    print("\nContact Records (.values()):")
    print(list(contacts.values()))

    print("\nContact Entries (.items()):")
    for name, details in contacts.items():
        print(name, "->", details)


# Main menu
while True:
    print("\n====== CONTACT MANAGEMENT SYSTEM ======")
    print("1. Add Contact")
    print("2. Display All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Display Dictionary Methods")
    print("7. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_contact()

    elif choice == "2":
        display_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        dictionary_methods()

    elif choice == "7":
        print("Exiting Contact Management System. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")

