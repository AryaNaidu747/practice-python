'''
Mini Project: Command-Line Contact Book
User can:
Add contacts, Search contacts, View all contacts, Delete contacts, Quit
Each contact stores:
Name, Phone number, Email
'''

contacts = []

while True: 
  starting_input = input("Enter 1 for new contact, 2 to search contact, 3 to view contact, 4 to delete contact, 5 to quit: ")

  if starting_input == "1":
    name = input("Enter a name: ").strip().title()
    phone = input("Enter a phone number in format XXX-XXX-XXXX: ")
    email = input("Enter an email in format email@address.xxx: ")

    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)

    print("Contact added")

  if starting_input == "2":
    search_name = input("Enter contact name: ").strip().title()

    found = False

    for contact in contacts:
      if contact["name"] == search_name:
        print(f'{contact["name"]}, {contact["phone"]}, {contact["email"]}')
        found = True

    if found == False:
      print("Contact not found")

  if starting_input == "3":
    if len(contacts) == 0:
      print("No contacts")

    for contact in contacts:
      print(f'{contact["name"]}, {contact["phone"]}, {contact["email"]}')

  if starting_input == "4":
    delete_name = input("Enter contact name to delete: ").strip().title()

    found = False

    for contact in contacts:
      if contact["name"] == delete_name:
        contacts.remove(contact)
        print("Contact deleted")
        found = True
        break

    if found == False:
      print("Contact not found")

  if starting_input == "5":
    break
