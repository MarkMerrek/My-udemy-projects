# Store info about films
films = {
    "Saw": [18, 5],
    "Greatest Showman": [12, 5],
    "Dune: Part Two": [16, 5],
    "Fight Club": [16, 5],
    "Oppenheimer": [16, 5],
    "Barbie": [12, 5],
    "Pulp Fiction": [18, 5],
    "Finding Dory": [3, 5],
    "Bourne": [18, 5],
    "Tarzan": [15, 5],
    "Ghost Busters": [12, 5]
}

while True:
    # Ask about film the user would like to watch
    choice = input("What film would you like to watch?: ").strip().title()

    # Film is in the dictionary
    if choice in films:
        # Ask about age
        age = int(input("How old are you?: ").strip())

        # Check age
        if age >= films[choice][0]:

            # Check enough seats
            num_seats = films[choice][1]

            if num_seats > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry, we are sold out!")

        else:
            print("You are too young to see that film!")

    # Film is not in the dictionary
    else:
        print("We don't have that film...")
