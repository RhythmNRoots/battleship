def draw_map(grid):
    """This function prints any grid (empty or containing ships) formed as list of lists into a map, visually more similar to battleship game"""
    for row in grid:
        for element in row:
            print(element, end = ' ') # printing each element, of the list (row), ending without new line.
        print('') # printing a new line, when row is ready
    return grid # returning the original grid (list of lists)

def adding_ships(grid, coordinates):
    """This function overwrites any grid with 'x', symbolizing ships at locations, defined by coordinates"""
    (first_x, first_y), (second_x, second_y), (third_x, third_y) = coordinates # unpacking the coordinates (list of tuples)
    grid[first_x][first_y] = 'x' # overwriting the grid at specific coordinates
    grid[second_x][second_y] = 'x'
    grid[third_x][third_y] = 'x'
    return(grid) # returning the modified grid (list of lists)

def ship_coordinate_user():
    defined_coordinates = input('Enter the coordinates of the ships (In this format (x1,y1), (x2,y2)):')
    
    # Splitting input string into a list (if no space between ')' and ',' )
    if '),' in defined_coordinates:
        defined_coordinates = defined_coordinates.split('),')
    # Splitting input string into a list (if there is space between ')' and ',' )
    elif ') ,' in defined_coordinates:
        defined_coordinates = defined_coordinates.split(') ,')
    
    #Turning input coordinates into list of tuples (containing integers)
    i=0 # counter of coordinate pairs
    for coordinate_pair in defined_coordinates:
        # Stripping white space, '(' and ')' from all coordinate pairs
        coordinate_pair = coordinate_pair.strip()
        coordinate_pair = coordinate_pair.strip('(')
        coordinate_pair = coordinate_pair.strip(')')
        
        # Splitting coordinate pair string into a list
        coordinate_pair = coordinate_pair.split(',') 
        j = 0 # counter of coordinate (x, y)
        for coordinate in coordinate_pair:
            coordinate = int(coordinate) # Turning defined coordinate to integer
            coordinate_pair[j] = coordinate # Redefining list element
            j = j + 1
        coordinate_pair = tuple(coordinate_pair) # Turning coordinate list to tuple
        defined_coordinates[i] = coordinate_pair # Redefining list element
        i = i + 1
    return(defined_coordinates)

def beginning_of_game():
    """This function initializes the game, by adding the ships to the empty grid, to locations, defined by coordinates."""
    empty_grid = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
    ship_coordinates_user = ship_coordinate_user()
    # later the coordinates should be a result of an input --> ship_coordinates_user = input('Enter the coordinates of the ships: ')
    # and then the input should be converted to a list of tuples (containing integers)
    user_grid = adding_ships(empty_grid, ship_coordinates_user)
    draw_map(user_grid)

beginning_of_game()
