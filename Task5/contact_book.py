contacts = {}
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    print("\nContact added successfully!")
def view_contacts():
    if not contacts:
        print("\nNo contacts found.")
        return
    print("\n----- Contact List -----")
    for name, details in contacts.items():
        print(f"{name} - {details['Phone']}")
def search_contact():
    search = input("\nEnter Name or Phone Number: ")
    for name, details in contacts.items():
        if search.lower() == name.lower() or search == details["Phone"]:
            print("\nContact Found")
            print("Name:", name)
            print("Phone:", details["Phone"])
            print("Email:", details["Email"])
            print("Address:", details["Address"])
            return
    print("Contact not found.")
def update_contact():
    name = input("\nEnter contact name to update: ")
    if name in contacts:
        contacts[name]["Phone"] = input("New Phone: ")
        contacts[name]["Email"] = input("New Email: ")
        contacts[name]["Address"] = input("New Address: ")
        print("Contact updated successfully!")
    else:
        print("Contact not found.")
def delete_contact():
    name = input("\nEnter contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")
while True:
    print("\n========== CONTACT BOOK ==========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("\nEnter your choice: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("\nThank you for using Contact Book!")
        break
    else:
        print("Invalid Choice!")
