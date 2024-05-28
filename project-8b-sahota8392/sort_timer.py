# Author: Harpreet Sahota
# GitHub: sahota8392
# Date: 8/2/23
# Description: create graph with bubble and insert sort methods

import time
import random
import functools

# installed matplotlib package
from matplotlib import pyplot


def sort_timer(func):
    """decorator function returns the elapsed time - will be used with bubble/insertion methods"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper for sort_timer"""
        t1 = time.perf_counter()
        func(*args, **kwargs)
        t2 = time.perf_counter()

        elapsed_time = t2 - t1
        return elapsed_time

    return wrapper


@sort_timer
def bubble_sort(a_list):
    """Bubble sort method from module 4"""
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp


@sort_timer
def insertion_sort(a_list):
    """Insertion sort method from module 4"""
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value


def make_lists_of_sort_times(sort_1, sort_2, list_length):
    """
    3 parameters - 2 functions and 1 length list of integers
    returns (tuple) two lists of time
    one for each sort algorithm
    """

    def create_random_list(length):
        """helper for random list length"""
        return [random.randint(1, 10001) for _ in range(length)]  # random module generates random number 1<=r<=10000

    bubble_time = []
    insertion_time = []

    for length in list_length:
        random_list = create_random_list(length)  # random list

        # random list being copied for bubble and insertion
        b_list = list(random_list[:])
        i_list = list(random_list[:])

        # Measure time for bubble
        elapse_time_b = sort_1(b_list)
        bubble_time.append(elapse_time_b)

        # Measure time for insertion
        elapse_time_i = sort_2(i_list)
        insertion_time.append(elapse_time_i)
    return bubble_time, insertion_time


def compare_sorts(sort_1, sort_2):
    """compares insertion and bubble sort times"""
    lengths = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    bubble_time, insertion_time = make_lists_of_sort_times(sort_1, sort_2, lengths)

    pyplot.plot(lengths, bubble_time, 'ro--', linewidth=2, label='Bubble Sort')
    pyplot.plot(lengths, insertion_time, 'go--', linewidth=2, label='Insertion Sort')

    pyplot.xlabel("Size of List Being Sorted")
    pyplot.ylabel("Seconds to Sort")

    pyplot.legend(loc='upper left')
    pyplot.show()


compare_sorts(bubble_sort, insertion_sort)

# # test to confirm matplotlib.pyplot was installed and functions correctly
# data = (3, 6, 9, 12, 15)
# fig, simple_chart = matplotlib.pyplot.subplots()
# simple_chart.plot(data)
# matplotlib.pyplot.show()
