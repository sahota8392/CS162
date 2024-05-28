# Author:  Harpreet Sahota
# GitHub:  Sahota8392
# Date:  7/11/2023
# Description:  Insertion sort method to sort list of Boxes from greatest to lowest volume

class Box:
    """
    Box class initializing length, width, height
    To calculate the volume of the Box
    """

    def __init__(self, length, width, height):
        """initial 3 values: length, width, height"""
        self._length = length
        self._width = width
        self._height = height

    def get_length(self):
        """gets the length of Box"""
        return self._length

    def get_width(self):
        """gets the width of Box"""
        return self._width

    def get_height(self):
        """gets the height of Box"""
        return self._height

    def volume(self):
        """returns the volume of the Box"""
        volume = self.get_length() * self.get_width() * self.get_height()
        return volume


def box_sort(box_list):
    """Insertion Sort method from greatest to lowest volume"""
    for index in range(1, len(box_list)):
        value = box_list[index]
        pos = index - 1
        while pos >= 0 and box_list[pos].volume() < value.volume():
            box_list[pos + 1] = box_list[pos]
            pos -= 1
        box_list[pos + 1] = value

    for box in box_list:
        print(box.volume())


# b1 = Box(3.4, 19.8, 2.1)
# b2 = Box(1.0, 1.0, 1.0)
# b3 = Box(8.2, 8.2, 4.5)
#
# box_list = [b1, b2, b3]
# box_sort(box_list)
