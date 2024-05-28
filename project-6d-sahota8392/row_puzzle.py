# Author: Harpreet Sahota
# GitHub: sahota8392
# Date: 7/22/23
# Description: Recursive function taking list of integers and returns True if puzzle is solvable for that row

def row_puzzle(row, position=0, marked=None):
    """
     Recursive function returns true if the puzzle can be solved
     Starts at index 0 and must end in the last index without repeating an index

     [2, 4, 5, 3, 1, 4, 0] values
     [0, 1, 2, 3, 4, 5, 6] index

     position default argument position set at index 0
     marked will keep track if we have visited an index or not
    """

    if marked is None:  # makes a set of the visited index
        marked = set()

    if position < 0 or position >= len(row) or position in marked:  # check if it's out of bounds or marked
        return False

    if row[position] == 0 and position == len(row) - 1:  # if it's index is 0 and not more in row
        return True

    if position not in marked:  # check if position is not in the marked set, add to it
        marked.add(position)

    move_right = row_puzzle(row, position + row[position], marked)
    move_left = row_puzzle(row, position - row[position], marked)

    if move_left or move_right:  # checks if left is visited or right is visited and executes left or right
        return True
    return False

#
# t = [1]  # false, not 0
# print('t:f', row_puzzle(t))
#
# t0 = [0]  # true
# print('t0: t', row_puzzle(t0))
#
# t1 = [2, 5, 0]  # true
# print('t1: t', row_puzzle(t1))
#
# t2 = [1, 3, 2, 1, 3, 4, 0]  # false
# print('t2: f', row_puzzle(t2))
#
# t3 = [1, 4, 3, 1, 2, 2, 0]  # true
# print('t3: t', row_puzzle(t3))
#
# t4 = [4, 1, 6, 1, 2, 4, 3, 2, 0]  # true
# print('t4: t', row_puzzle(t4))
#
# t5 = [3, 2, 4, 1, 1, 2, 0]  # true
# print('t5: t', row_puzzle(t5))
#
# t6 = [3, 1, 0, 1, 3, 2, 3, 0]  # true
# print('t6: t', row_puzzle(t6))
#
# t7 = [3, 1, 2, 2, 2, 0, 2, 3, 0]  # true
# print('t7: t', row_puzzle(t7))
#
# t8 = [3, 0, 2, 1, 2, 3, 0]  # true
# print('t8: t', row_puzzle(t8))
#
# t9 = [3, 0, 2, 1, 2, 3, 1, 0, 0]  # true
# print('t9: t', row_puzzle(t9))
#
# t10 = [2, 0, 5, 3, 1, 3, 1, 4, 0]
# print('t10: t', row_puzzle(t10))
#
# t11 = [2, 4, 5, 3, 1, 3, 1, 4, 0]  # true
# print('t11: t', row_puzzle(t11))
#
# t12 = [1, 3, 2, 1, 3, 4, 0]  # false
# print('t12: f', row_puzzle(t12))
