# Author: Harpreet Sahota
# GitHub username: sahota8392
# Date: 6/26/23
# Description: Function to return mean, median and mode of student grades


from statistics import mean, median, mode


class Student:
    """Student class"""

    def __init__(self, name, grade):
        """Creates student with name and grade parameters"""
        self._name = name
        self._grade = grade

    def get_name(self):
        """Returns student name"""
        return self._name

    def get_grade(self):
        """Returns student grade"""
        return self._grade


def basic_stats(list_student):
    """Mean, Median, Mode function"""
    grades = [student.get_grade() for student in list_student]
    return mean(grades), median(grades), mode(grades)


s1 = Student("Kyoungmin", 73)
s2 = Student("Mercedes", 74)
s3 = Student("Avanika", 78)
s4 = Student("Marta", 74)

student_list = [s1, s2, s3, s4]
print(basic_stats(student_list))  # should print a tuple of three values
