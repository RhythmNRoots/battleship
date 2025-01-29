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

def beginning_of_game():
    """This function initializes the game, by adding the ships to the empty grid, to locations, defined by coordinates."""
    empty_grid = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    ship_coordinates_user = [(0, 0), (0, 2), (2, 1)]
    # later the coordinates should be a result of an input --> ship_coordinates_user = input('Enter the coordinates of the ships: ')
    # and then the input should be converted to a list of tuples (containing integers)
    user_grid = adding_ships(empty_grid, ship_coordinates_user)
    draw_map(user_grid)

# coordinate_test = input('Enter the coordinates of the ships:')

# Turning input coordinates into tuples
# coordinate_test = tuple(coordinate_test)
# for element in coordinate_test:
#     element = tuple(int(element))
#     print(type(element))
# print(type(coordinate_test))

beginning_of_game()
