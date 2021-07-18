"""
    Given two list of student heights, R & B,
    representing a row of students,
    
    Check if students can be arranged in an order
    that is satisfying the below rules:
        - Each student should stay in the same row.
        - Each student in the back row should be strictly
        taller than the student in front of him (in the front row.)

    R and B are of equal size and each has at least 2 students.
"""
from typing import List


def classPhotos(R: List[int], B: List[int]) -> bool:
    # We have to sort the arrays first.
    R.sort()
    B.sort()

    # If the two tallest guys are of equal height,
    # the photo can not be taken.
    if R[-1] == B[-1]:
        return False

    # Front row & back row 
    back_row = R if R[-1] > B[-1] else B
    front_row = R if R[-1] < B[-1] else B

    # If the guy in the back row in each
    # index is not taller than the the one 
    # in front of him, the photo can not 
    # be taken.
    for i in range(len(back_row)):
        if back_row[i] <= front_row[i]:
            return False
    return True
