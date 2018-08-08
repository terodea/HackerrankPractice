"""
https://www.hackerrank.com/challenges/grading/problem
"""
import os
import sys

def gradingStudents(grades):
    return [(g+5 - g%5 if g%5 > 2 and g>37 else g) for g in grades]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    grades = []
    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)
    result = gradingStudents(grades)
    f.write('\n'.join(map(str, result)))
    f.write('\n')
    f.close()
