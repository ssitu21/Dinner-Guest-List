# guest_list.py

guests = []


def add_guest():
    name = input("Enter guests name: ")
    # Clean up the name
    name = name.strip().title()
    guests.append(name)
    print(f"Added {name} to the list")


# Test
add_guest()
print("Guests:", guests)
