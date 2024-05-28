# Author: Harpreet Sahota
# GitHub: sahota8392
# Date: 7/20/23
# Description: Recursive function returns True if list is decreasing otherwise False

def is_decreasing(num_list, start=0):
    """recursive function that returns true if numbers in list are decreasing otherwise false"""

    if len(num_list) == 2:  # base case when only 2 elements in given list
        return num_list[0] > num_list[1]

    if len(num_list) > 2:  # iterates through the list checking if each element is less than preceding element
        element_1 = num_list[0]
        other_el = num_list[1:]
        element_2 = other_el[0]

        if element_1 > element_2:
            return is_decreasing(other_el)
    return False

# two_el_f = [2, 4]  # False
# print(is_decreasing(two_el_f))
#
# two_el_t = [4, 0]  # True
# print(is_decreasing(two_el_t))
#
# pos = [10, 9, 8, 7, 20, 6, 5, 4, 3, 2, 1]  # False
# print(is_decreasing(pos))
#
# neg = [-3.2, -6, -1, 0, 0, ]  # False
# print(is_decreasing(neg))

# num = [5, 4, 3, 2.2, 2.2, 1, 0, -2, -2.4]   # False
# print(is_decreasing(num))
