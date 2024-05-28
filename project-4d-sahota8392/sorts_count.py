# Author: Harpreet Sahota
# GitHub: sahota8392
# Date: 7/11/23
# Description: Write bubble sort that counts number of comparisons and number of exchanges while sorting list

def bubble_count(a_list):
    """use bubble sort on the a_list"""
    comparison = 0
    exchange = 0

    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            comparison += 1
            if a_list[index] > a_list[index + 1]:
                # comparison += 1
                exchange += 1
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp
    return comparison, exchange


def insertion_count(b_list):
    """use insertion sort on the b_list"""
    comparison = 0
    exchange = 0
    for index in range(1, len(b_list)):
        value = b_list[index]
        pos = index - 1
        while pos >= 0:
            comparison += 1
            if b_list[pos] > value:
                b_list[pos + 1] = b_list[pos]
                exchange += 1
                pos -= 1
            else:
                break
        b_list[pos + 1] = value
    return comparison, exchange


# a_list = [23, 5, 87, 16, 44, -9, 0, 31, 11, 88, 97, 64]
# a_list = range(100)
# print("bubble_count: ", bubble_count(a_list))
#
# b_list = [10, 0, -1]
# print("insertion_count: ", insertion_count(b_list))
