def draw_map(grid):
    for row in grid:
        for element in row:
            print(element, end = ' ')
        print('')
    return grid

def adding_ships(grid, coordinates):
    (first_x, first_y), (second_x, second_y), (third_x, third_y) = coordinates
    grid[first_x][first_y] = 'x'
    grid[second_x][second_y] = 'x'
    grid[third_x][third_y] = 'x'
    return(grid)

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
