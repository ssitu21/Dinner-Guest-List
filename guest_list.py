# guest_list.py

guests = []


def add_guest():
    name = input("Enter guest name: ")
    guests.append(name)
    print(f"Added {name} to the list")


# test
add_guest()
print("Current guests:", guests)
