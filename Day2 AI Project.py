contacts={}

def add_contact(name, number):
    contacts[name]=number
    print(f"contact {name} has been added.")
def update_contact(name, number):
    if name in contacts:
        contacts[name]=number
        print(f"contact {name} has been added.")
    else:
        print("{name} does not exist.")
def delete_contact(name):
    if name in contacts:
        contacts.pop(name)
        print(f"{name} has been deleted.")
    else:
        print(f"No contact found.")
def search_contact(name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"{name} does not exist.")
def display_contact():
    if contacts:
        print("Contact:")
        for name in sorted(contacts):
            print(f"{name}: {contacts[name]}\n")
    else:
        print("No contact found.")

while True:
    print("\nSelect one option from the below:")
    print("1.Add Contact\n2.Update Contact\n3.Delete Contact\n4.Search Contact\n5.Display Contact\n6.Exist\n")
    choice=input("Enter your option: ")
    if choice=='1':
        name=input("Enter name: ")
        number=input("Enter Contact Number: ")
        add_contact(name, number)
    elif choice=='2':
        name=input("Enter name: ")
        number=input("Enter Contact Number: ")
        update_contact(name, number)
    elif choice=='3':
        name=input("Enter name to delete: ")
        delete_contact(name)
    elif choice=='4':
        name=input("Enter name to search: ")
        search_contact(name)
    elif choice=='5':
        display_contact()
    elif choice=='6':
        break
    else:
        print("Invalid Selection...")