# guest_list.py

guests = []


def add_guest():
    name = input("Enter guest name: ")
    name = name.strip().title()

    if not name:
        print("Cant add empty name!")
    elif name in guests:
        print(f"{name} is already in the list!")
    else:
        guests.append(name)
        print(f"Added {name} to the list")


def show_guests():
    if not guests:
        print("Guest list is empty")
    else:
        print("\nCurrent Guests:")
        for i, guest in enumerate(guests, 1):
            print(f"{i}. {guest}")


# Test
add_guest()
show_guests()
