import random
import time


def draw_map(grid):
    """This function prints any grid (empty or containing ships) formed as list of lists into a map, visually more similar to battleship game"""
    for row in grid:
        for element in row:
            print(
                element, end=" "
            )  # printing each element, of the list (row), ending without new line.
        print("")  # printing a new line, when row is ready
    return grid  # returning the original grid (list of lists)


def adding_ships(grid, coordinates):
    """This function overwrites any grid with 'x', symbolizing ships at locations, defined by coordinates"""
    # Here the number of ships should be defined,  number of coordinate should match
    for element in coordinates:  # looping through all coordinates
        (x, y) = element  # unpacking the coordinates
        grid[y][x] = "x"  # overwriting the grid at specific coordinates
    return grid  # returning the modified grid (list of lists)


def getting_ship_coordinates_user(number_of_ships):
    """This function asks for an input from the user and converts the input to a list of tuple of integers, which are the coordinates for the user's ships during the game"""
    # Asking for an input to define all ship coordinates (variable contains a string at this point)
    user_ship_coordinates_all = input(
        f"Enter the coordinates of {number_of_ships} ships (In this format (x1,y1), (x2,y2), (x3, y3),...):"
    )

    # Splitting input string into a list (if no space between ')' and ',' )
    if ")," in user_ship_coordinates_all:
        user_ship_coordinates_all = user_ship_coordinates_all.split("),")
    # Splitting input string into a list (if there is space between ')' and ',' )
    elif ") ," in user_ship_coordinates_all:
        user_ship_coordinates_all = user_ship_coordinates_all.split(") ,")

    # Turning input coordinates into list of tuples (containing integers)
    i = 0  # counter of x-y coordinates
    for ship_coordinates in user_ship_coordinates_all:
        # Stripping white space, '(' and ')' from all coordinate pairs
        ship_coordinates = ship_coordinates.strip()
        ship_coordinates = ship_coordinates.strip("(")
        ship_coordinates = ship_coordinates.strip(")")

        # Splitting coordinate pair string into a list
        ship_coordinates = ship_coordinates.split(",")
        j = 0  # counter of coordinate (x, y)
        for coordinate in ship_coordinates:
            try:
                coordinate = int(coordinate)  # Turning defined coordinate to integer
            except ValueError:
                raise ValueError(
                    "Please enter only integers as coordinates."
                )  # If coordinate is not an integer error is raised and the program is ended.
            if 0 <= coordinate <= 9:
                pass
            else:
                raise ValueError(
                    "Coordinate is not in expected range."
                )  # If number is not in range (0-9) error is raised and the program is ended.
            ship_coordinates[j] = coordinate  # Redefining list element
            j = j + 1
        ship_coordinates = tuple(ship_coordinates)  # Turning coordinate list to tuple
        if ship_coordinates in user_ship_coordinates_all:
            raise ValueError(f"Coordinate {ship_coordinates} is already occupied.")
        user_ship_coordinates_all[i] = ship_coordinates  # Redefining list element
        i = i + 1
    return user_ship_coordinates_all


def getting_ship_coordinates_computer(number_of_ships):
    """This function randomly selects the coordinates for the computer's ships and creates a list of tuples of integers"""
    computer_ship_coordinates_all = []  # Creating the empty list
    for ships in range(number_of_ships):  # Iteration for the number of ships
        ship_coordinates = (
            random.randrange(10),
            random.randrange(10),
        )  # Random number (0-9) in a tuple
        while (
            ship_coordinates in computer_ship_coordinates_all
        ):  # While the random coordinates are already used
            ship_coordinates = (
                random.randrange(10),
                random.randrange(10),
            )  # Redefining ship coordinates (Random number (0-9) in a tuple)
        computer_ship_coordinates_all.append(
            ship_coordinates
        )  # Appending the coordinate pair to the list
    return computer_ship_coordinates_all


def get_user_shooting_coordinates():
    while True:
        user_shooting_coordinates_str = input(
            "Enter the coordinates for the target. In format (x, y)"
        )
        try:
            user_shooting_coordinates = eval(user_shooting_coordinates_str)
            if (
                isinstance(user_shooting_coordinates, tuple)
                and len(user_shooting_coordinates) == 2
                and 0 <= user_shooting_coordinates[0] < 10
                and 0 <= user_shooting_coordinates[1] < 10
            ):
                break
        except:
            print("Please enter the coordinates in format (x, y)")

    return user_shooting_coordinates


def get_computer_shooting_coordinates():
    computer_shooting_coordinates = (random.randrange(10), random.randrange(10))
    return computer_shooting_coordinates


def beginning_of_game():
    """This function initializes the game, by adding the ships to the empty grid, to locations, defined by coordinates."""
    empty_grid_for_user = [
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]
    empty_grid_for_computer = [
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]

    # First: Deciding the number of ships and the coordinates for user and computer
    while True:
        selected_ship_number = input("How many ships do you want to play with? ")
        try:
            selected_ship_number = int(selected_ship_number)
            break
        except ValueError:
            print("Please enter an integer.")
    ship_coordinates_user = getting_ship_coordinates_user(selected_ship_number)
    ship_coordinates_computer = getting_ship_coordinates_computer(selected_ship_number)

    # Second: drawing the game
    user_grid = adding_ships(empty_grid_for_user, ship_coordinates_user)
    print("_user_")
    draw_map(user_grid)
    computer_grid = adding_ships(empty_grid_for_computer, ship_coordinates_computer)
    print("_computer_")
    draw_map(computer_grid)

    # Third: shooting
    while True:
        user_shooting_coords = get_user_shooting_coordinates()
        print(f"User shoots at position {user_shooting_coords}")
        if user_shooting_coords in ship_coordinates_computer:
            ship_coordinates_computer.remove(user_shooting_coords)
            print("  -> It was a hit!")
        else:
            print("  -> It was a miss!")
        if len(ship_coordinates_computer) == 0:
            print("All opponents ships have been destoryed, you have won!")
            break

        time.sleep(2)

        computer_shooting_coords = get_computer_shooting_coordinates()
        print(f"Computer shoots at position {computer_shooting_coords}")
        if computer_shooting_coords in ship_coordinates_user:
            ship_coordinates_user.remove(computer_shooting_coords)
            print("  -> It was a hit!")
        else:
            print("  -> It was a miss!")
        if len(ship_coordinates_user) == 0:
            print("All opponents ships have been destoryed, the computer has won!")
            break


beginning_of_game()
