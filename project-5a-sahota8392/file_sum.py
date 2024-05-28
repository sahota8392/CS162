# Author:  Harpreet Sahota
# GitHub:  Sahota8392
# Date:  7/14/2023
# Description:  Read number file and write a total sum value file

def file_sum(numbers):
    """Read numbers from the file and create a new file with the sum value only"""
    try:
        with open(numbers, 'r') as infile:
            num_integer = [float(num.strip()) for num in infile.readlines()]
            print(num_integer)

        with open('sum.txt', 'w') as outfile:
            total = sum(num_integer)
            outfile.write(str(total))

    except FileNotFoundError:
        print('File not found.')
