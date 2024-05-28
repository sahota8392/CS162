# Author: Harpreet Sahota
# GitHub: sahota8392
# Date: 7/21/23
# Description: Recursive function returns true if first string is subsequence of second string

def is_subsequence(s1, s2):
    """recursive function with 2 string parameters
    return True if string 1 is subsequence of second string"""
    if len(s1) == 0:  # if s1 is empty string
        return True
    if s1 in s2:  # if s1 and s2 are same
        return True
    if len(s2) == 0 and len(s1) != 0:  # if s1 is not empty and s2 is empty
        return False
    if s1[0] == s2[0]:
        return is_subsequence(s1[1:], s2[1:])
    return is_subsequence(s1, s2[1:])


# s1 = ''  # empty string - return True
# s2 = 'american tour'
# print('True', is_subsequence(s1, s2))
#
# s1 = 'same as other'  # identical strings - return True
# s2 = 'same as other'
# print('True', is_subsequence(s1, s2))
#
# s1 = 'aeiou'  # return True
# s2 = 'american tour'
# print('True', is_subsequence(s1, s2))
#
# s1 = 'taim'  # return False
# s2 = 'tain'
# print('False', is_subsequence(s1, s2))
#
# s1 = 'aeiou'
# s2 = 'aerosauce'
# print('False', is_subsequence(s1, s2))
