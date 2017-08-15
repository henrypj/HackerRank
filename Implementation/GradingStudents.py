import sys

def solve(grades):
    # Complete this function
    roundedGrades = []
    for grade in grades:
        if (grade < 38) or (grade % 5 == 0):
            roundedGrades.append(grade)
        else:
            i = 1
            rounded = False
            while i < 3:
                if (grade + i) % 5 == 0:
                    roundedGrades.append(grade + i)
                    rounded = True
                i += 1
            if not rounded:
                roundedGrades.append(grade)
    return roundedGrades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))