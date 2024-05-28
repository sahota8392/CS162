# Author:  Harpreet Sahota
# GitHub:  Sahota8392
# Date:  7/11/2023
# Description:  Modify Binary Search to raise exception than return -1

class TargetNotFound(Exception):
    """Exception raised when target is not in the binary search list"""
    pass

def bin_except(a_list, target):
    """
    Searches the a_list for the target value
    If found, returns the index of position
    If not found, raise exception than return -1
    """
    first = 0
    last = len(a_list) - 1
    while first <= last:
        middle = (first + last) // 2
        if a_list[middle] == target:
            return middle
        if a_list[middle] > target:
            last = middle - 1
        else:
            first = middle + 1
    # return -1
    raise TargetNotFound


try:
    search_list = [1, 10, 20, 21, 2, 4, 15, 83]
    result = bin_except(search_list, 21)
    print('Target at index:', result)
except TargetNotFound:
    print('Target is not found in the list')
finally:
    print('Binary Search Complete')
