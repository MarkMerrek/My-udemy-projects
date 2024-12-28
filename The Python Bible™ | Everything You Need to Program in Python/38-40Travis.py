# List of known users
known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry", "Masha"]

while True:
    # Introduce Travis
    print("Hi! My name is Travis")
    # Ask for your name
    name = input("What is your name?: ").strip().capitalize()

    # If name is in the list
    if name in known_users:
        print("Hello {}!".format(name))
        # Ask if you want to be removed from the list
        remove = input("Would you like to be removed from the system (y/n)?: ").strip().lower()

        # Remove from the list
        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("No problem, I didn't want you to leave anyway!")

    # If name isn't in the list
    else:
        print("Hmmm I don't think I have met you yet {}".format(name))
        # Ask if you want to be added to the list
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()

        # Add to the list
        if add_me == "y":
            known_users.append(name)
        elif add_me == "n":
            print("No worries, see you around!")
