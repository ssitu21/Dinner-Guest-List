# guest_list.py

guests = []


def add_guest():
    name = input("Enter guest name: ")
    name = name.strip().title()

    # Check for duplicates
    if name in guests:
        print(f"{name} is already in the list!")
    else:
        guests.append(name)
        print(f"Added {name} to the list")


# Test
add_guest()  # same name twice
print("Guests:", guests)
