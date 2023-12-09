def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact {name} updated with new phone: {new_phone}."
    else:
        return f"Contact {name} not found."
def list_all_contacts(args, contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts available."
def get_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"The phone number for {name} is: {contacts[name]}."
    else:
        return f"Contact {name} not found."
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(list_all_contacts(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()