import function_2048

# Test
import copy
import random

matrix = []
# Create a empty matrix
for i in range(function_2048.size):
    row = []
    for j in range(function_2048.size):
        row.append(0)
    matrix.append(row)

# Initialize the game by enter two number two into the matrix
needadd = 2
while needadd > 0:
    rowNum = random.randint(0, function_2048.size - 1)
    colNum = random.randint(0, function_2048.size - 1)
    if matrix[rowNum][colNum] == 0:
        matrix[rowNum][colNum] = function_2048.add_new()
        needadd -= 1 #### Try

print("Welcome to 2048! Valid input including 'w'(merge up), 'a'(merge left), 's'(merge down) or d(merge right).")
function_2048.display(matrix)

# Then we use loop to ask user to input moves
gameover = False
while not gameover:
    move = input('Enter instructions.')
    valid = True

    tempMatrix = copy.deepcopy(matrix)

    if move == 'd' or move == 'D':
        matrix = function_2048.merge_right(matrix)
    elif move == 'w' or move == 'W':
        matrix = function_2048.merge_up(matrix)
    elif move == 'a' or move == 'A':
        matrix = function_2048.merge_left(matrix)
    elif move == 's' or move == 'S':
        matrix = function_2048.merge_down(matrix)
    else:
        valid = False

    if not valid:
        print('Please enter a valid input')
    else:
        # check if the move is useless
        if matrix == tempMatrix:
            print('Try another input.')
        else:
            if function_2048.if_win(matrix):
                function_2048.display(matrix)
                print('You won!!!')
                gameover = True
            else:
                function_2048.add_value(matrix)
                function_2048.display(matrix)
                if function_2048.if_lose(matrix):
                    print('Sorry, you lost the game.')
                    gameover = True