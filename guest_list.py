# guest_list.py

guests = []


def add_guest():
    name = input("Enter guest name: ")
    name = name.strip().title()

    if not name:
        print("Can't add empty name!")
    elif name in guests:
        print(f"{name} is already in the list!")
    else:
        guests.append(name)
        print(f"Added {name} to the list")


def remove_guest():
    name = input("Enter name to remove: ")
    name = name.strip().title()

    if name in guests:
        guests.remove(name)
        print(f"Removed {name} from the list")
    else:
        print(f"{name} not found in the list")


def sort_guests():
    guests.sort()
    print("Guest list sorted!")


def show_guests():
    if not guests:
        print("Guest list is empty")
    else:
        print(f"\nTotal guests: {len(guests)}")
        for i, guest in enumerate(guests, 1):
            print(f"{i}. {guest}")


def show_menu():
    print("GUEST LIST MANAGER")
    print("1. Add guest")
    print("2. Remove guest")
    print("3. Sort guests")
    print("4. Show all guests")
    print("5. Exit")


# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_guest()
    elif choice == "2":
        remove_guest()
    elif choice == "3":
        sort_guests()
    elif choice == "4":
        show_guests()
    elif choice == "5":
        print("Bye")
        break
    else:
        print("Invalid, try again")

    input("\nPress Enter to continue...")
