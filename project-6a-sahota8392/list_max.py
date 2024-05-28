# Author: Harpreet Sahota
# GitHub: sahota8392
# Date: 7/20/23
# Description: Recursive function that returns max value in a given list

def list_max(num_list, start=0, end=None):
    """recursive function returning the max value in the given list parameter
    default arguments for start = 0 and end at None
    """

    if len(num_list) == 1:  # base case when there is only 1 element in the list
        return num_list[0]

    if len(num_list) > 1:  # iterates through the list of numbers
        element_1 = num_list[0]
        other_elements = num_list[1:]
        max_num = list_max(other_elements)

        if element_1 > max_num: # compare element 1 to max num and return the max number
            return element_1
        return max_num


numbers = [0, 3.14, -2, -1000, 25, 25, 1.2]
print(list_max(numbers))

neg = [-11, -10, -50, -1.2]
print(list_max(neg))

dec = [3.14, 3.143, 3.144]
print(list_max(dec))

check = [10, 0, 5, 45, 00, 1]
print(list_max(check))
