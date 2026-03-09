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
        print("\nCurrent Guests:")
        for i, guest in enumerate(guests, 1):
            print(f"{i}. {guest}")


# Test sort
add_guest()
add_guest()
add_guest()
show_guests()
sort_guests()
show_guests()
