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

coordinate_test = input('Enter the coordinates of the ships:')

#Turning input coordinates into tuples
coordinate_test = tuple(coordinate_test)
for element in coordinate_test:
    element = tuple(int(element))
    print(type(element))
print(type(coordinate_test))


#def beginning_of_game():
#    empty_grid = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
#    coordinates_1 = input('ship positions:')
    #converting coordinates_1 to tuples
#    player_grid_1 = adding_ships(empty_grid, coordinates_1)
#    draw_map(player_grid_1)


#coordinate_1 = (1, 0)
#player_grid_1 = adding_ships(empty_grid, coordinate_1)
#draw_map(player_grid_1)
#print()
#coordinate_2 = (1, 1)
#player_grid_2 = adding_ships(player_grid_1, coordinate_2)
#draw_map(player_grid_2)

#(first_x, first_y), (second_x, second_y), (third_x, third_y) = coordinates
