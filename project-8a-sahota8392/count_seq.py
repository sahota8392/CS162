# Author: Harpreet Sahota
# GitHub: sahota8392
# Date: 8/02/23
# Description: Generator function that generates sequence

def count_seq():
    """Generator function with no arguments generates sequence of numbers"""
    first_term = '2'
    next_term = '12'
    yield first_term  # set the first and second terms, yield initial term

    while True:  # indefinite while loop yielding next term
        yield next_term

        current_term = next_term  # set current to next and next to blank, count starts at 1
        next_term = ''
        count = 1

        for num in range(1, len(current_term)):  # for loop from 1 to length of current term
            if current_term[num] == current_term[num - 1]:  # if current index is same as previous index, increase count
                count += 1
            else:
                next_term += str(count) + current_term[num - 1]  # if current index is not same as previous index
                count = 1
        next_term += str(count) + current_term[-1]


# my_gen = count_seq()
# for i in range(10):
#     print(next(my_gen))
