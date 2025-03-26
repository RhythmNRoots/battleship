import random

def draw_map(grid):
    """This function prints any grid (empty or containing ships) formed as list of lists into a map, visually more similar to battleship game"""
    for row in grid:
        for element in row:
            print(element, end = ' ') # printing each element, of the list (row), ending without new line.
        print('') # printing a new line, when row is ready
    return grid # returning the original grid (list of lists)

def adding_ships(grid, coordinates):
    """This function overwrites any grid with 'x', symbolizing ships at locations, defined by coordinates"""
    #Here the number of ships should be defined,  number of coordinate should match
    (first_x, first_y), (second_x, second_y), (third_x, third_y) = coordinates # unpacking the coordinates (list of tuples)
    grid[first_x][first_y] = 'x' # overwriting the grid at specific coordinates
    grid[second_x][second_y] = 'x'
    grid[third_x][third_y] = 'x'
    return(grid) # returning the modified grid (list of lists)

def getting_ship_coordinates_user():
    """This function asks for an input from the user and converts the input to a list of tuple of integers, which are the coordinates for the user's ships during the game"""
    # Asking for an input to define all ship coordinates (variable contains a string at this point)
    user_ship_coordinates_all = input('Enter the coordinates of three ships (In this format (x1,y1), (x2,y2), (x3, y3)):')
    
    # Splitting input string into a list (if no space between ')' and ',' )
    if '),' in user_ship_coordinates_all:
        user_ship_coordinates_all = user_ship_coordinates_all.split('),')
    # Splitting input string into a list (if there is space between ')' and ',' )
    elif ') ,' in user_ship_coordinates_all:
        user_ship_coordinates_all = user_ship_coordinates_all.split(') ,')
    
    #Turning input coordinates into list of tuples (containing integers)
    i=0 # counter of x-y coordinates
    for ship_coordinates in user_ship_coordinates_all:
        # Stripping white space, '(' and ')' from all coordinate pairs
        ship_coordinates = ship_coordinates.strip()
        ship_coordinates = ship_coordinates.strip('(')
        ship_coordinates = ship_coordinates.strip(')')
        
        # Splitting coordinate pair string into a list
        ship_coordinates = ship_coordinates.split(',') 
        j = 0 # counter of coordinate (x, y)
        for coordinate in ship_coordinates:
            try:
                coordinate = int(coordinate) # Turning defined coordinate to integer
            except ValueError:
                raise ValueError('Please enter only integers as coordinates.') # If coordinate is not an integer error is raised and the program is ended.
            if 0 <= coordinate <= 9:
                pass
            else:
                raise ValueError('Coordinate is not in expected range.') # If number is not in range (0-9) error is raised and the program is ended.
            ship_coordinates[j] = coordinate # Redefining list element
            j = j + 1
        ship_coordinates = tuple(ship_coordinates) # Turning coordinate list to tuple
        if ship_coordinates in user_ship_coordinates_all:
            raise ValueError(f'Coordinate {ship_coordinates} is already occupied.')
        user_ship_coordinates_all[i] = ship_coordinates # Redefining list element
        i = i + 1
    return(user_ship_coordinates_all)

def getting_ship_coordinates_computer():
    """This function randomly selects the coordinates for the computer's ships and creates a list of tuples of integers"""
    computer_ship_coordinates_all = [] # Creating the empty list
    for ships in range(3): # Iteration for the number of ships
        ship_coordinates = (random.randrange(10), random.randrange(10)) # Random number (0-9) in a tuple
        while ship_coordinates in computer_ship_coordinates_all: # While the random coordinates are already used
            ship_coordinates = (random.randrange(10), random.randrange(10)) # Redefining ship coordinates (Random number (0-9) in a tuple)
        computer_ship_coordinates_all.append(ship_coordinates) # Appending the coordinate pair to the list
    return(computer_ship_coordinates_all)

def beginning_of_game():
    """This function initializes the game, by adding the ships to the empty grid, to locations, defined by coordinates."""
    empty_grid_for_user = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
    empty_grid_for_computer = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
    ship_coordinates_user = getting_ship_coordinates_user()
    ship_coordinates_computer = getting_ship_coordinates_computer()
    user_grid = adding_ships(empty_grid_for_user, ship_coordinates_user)
    print("_user_")
    draw_map(user_grid)
    computer_grid = adding_ships(empty_grid_for_computer, ship_coordinates_computer)
    print("_computer_")
    draw_map(computer_grid)

beginning_of_game()