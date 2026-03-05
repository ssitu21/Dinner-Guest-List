# guest_list.py

guests = []


def add_guest():
    name = input("Enter guest name: ")
    name = name.strip().title()

    # Check if empty
    if not name:
        print("Cant add empty name!")
    # Check for duplicates
    elif name in guests:
        print(f"{name} is already in the list!")
    else:
        guests.append(name)
        print(f"Added {name} to the list")


# Test
add_guest()  # press enter
print("Guests:", guests)
