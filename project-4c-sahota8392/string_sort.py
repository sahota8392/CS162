# Author:  Harpreet Sahota
# GitHub:  Sahota8392
# Date:  7/11/2023
# Description:  Modify insertion sort to sort list of strings instead of numbers


def string_sort(string_list):
    """
    Sorts a_list in ascending order for strings
    """
    for index in range(1, len(string_list)):
        value = string_list[index]
        pos = index - 1
        while pos >= 0 and string_list[pos].lower() > value.lower():
            string_list[pos + 1] = string_list[pos]
            pos -= 1
        string_list[pos + 1] = value


# string_list = ['Zebra', 'apple', 'maRker', 'marble']
# print('Original:', string_list)
# string_sort(string_list)
# print('Modified:', string_list)
#
# string_list2 = ['Pizza', 'BurgER', 'BuRgERS', 'taCO', '0Sushi', '3pies']
# print('Original 2:', string_list2)
# string_sort(string_list2)
# print('Modified 2:', string_list2)
