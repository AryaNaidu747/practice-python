'''
Mini Project: Command-Line Contact Book
User can:
Add contacts, Search contacts, View all contacts, Delete contacts, Quit
Each contact stores:
Name, Phone number, Email
'''

'''
def add_contact():

def rem_contact():

def view_contact():

def delete_contact():
'''

contacts = []
while True: 
  starting_input =  input("Enter 1 for new contact, 2 to search contact, 3 to view contact, 4 to delete contact, 5 to quit: ")
  if starting_input == "1":
    name = input("Enter a name: ").strip().title()
    phone = input("Enter a phone number in format XXX-XXX-XXXX: ")
    email = input("Enter an email in format email@address.xxx: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
  if starting_input == "3":
    for contact in contacts:
      print(f"{contact["name"]}, {contact["phone"]}, {contact["email"]}")
      
  if starting_input == "5":
      break
