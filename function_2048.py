import random
import copy
size = 4


def display(matrix):
    # This function is used to create a board of current matrix in a more straightforward way
    largest = int(matrix[0][0])
    for i in range(len(matrix)):  # find the max value in matrix
        for j in range(len(matrix[i])):
            if int(matrix[i][j]) > largest:
                largest = matrix[i][j]
    space = len(str(largest))
    for row in matrix:  # Create some row with the same length for every element
        currRow = '|'
        for element in row:
            if element == 0:
                currRow += ' ' * space + '|'
            else:
                currRow += (' ' * (space - len(str(element)))) + str(element) + '|'
        print(currRow)
    print()


def merge_one_row_left(row):  # Merge one row left
    for j in range(size - 1):
        for i in range(size - 1, 0, -1):
            if row[i - 1] == 0:
                row[i - 1] = row[i]
                row[i] = 0
    for i in range(size - 1):
        if row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0
    for i in range(size - 1, 0, -1):
        if row[i - 1] == 0:
            row[i - 1] = row[i]
            row[i] = 0
    return row


def merge_left(curr_matrix):  # merge the matrix to the left
    for i in range(size):
        curr_matrix[i] = merge_one_row_left(curr_matrix[i])
    return curr_matrix


def reverse(row):  # reverse the order of one row
    new = []
    for i in range(size - 1, -1, -1):
        new.append(row[i])
    return new


def merge_right(curr_matrix):  # merge the matirx to right
    for i in range(size):
        curr_matrix[i] = reverse(curr_matrix[i])
        curr_matrix[i] = merge_one_row_left(curr_matrix[i])
        curr_matrix[i] = reverse(curr_matrix[i])
    return curr_matrix


def transpose(curr_matrix):  # This function is used simply to tranpose matrix
    for j in range(size):
        for i in range(j, size):
            if i != j:
                curr_matrix[i][j], curr_matrix[j][i] = curr_matrix[j][i], curr_matrix[i][j]
    return curr_matrix


def merge_up(curr_matrix):  # merge the matrix up
    curr_matrix = transpose(curr_matrix)
    curr_matrix = merge_left(curr_matrix)
    curr_matrix = transpose(curr_matrix)
    return curr_matrix


def merge_down(curr_matrix):  # merge the matrix down
    curr_matrix = transpose(curr_matrix)
    curr_matrix = merge_right(curr_matrix)
    curr_matrix = transpose(curr_matrix)
    return curr_matrix


def add_new():  # Randomly select 2(75%) or 4(25%)
    if random.randint(1, 4) == 1:
        return 4
    else:
        return 2


def add_value(matrix):  # add a new value in one empty cell of the matrix
    rowNum = random.randint(0, size - 1)
    colNum = random.randint(0, size - 1)
    while not matrix[rowNum][colNum] == 0:
        rowNum = random.randint(0, size - 1)
        colNum = random.randint(0, size - 1)
    matrix[rowNum][colNum] = add_new()


def if_win(matrix):
    for row in matrix:
        if 2048 in row:
            return True
    return False


def if_lose(matrix):
    temp1 = copy.deepcopy(matrix)
    temp2 = copy.deepcopy(matrix)
    temp1 = merge_down(temp1)
    if temp1 == temp2:
        temp1 = merge_up(temp1)
        if temp1 == temp2:
            temp1 = merge_right(temp1)
            if temp1 == temp2:
                temp1 = merge_left(temp1)
                if temp1 == temp2:
                    return True
    return False