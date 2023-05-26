#
def gradingAlgorithm(n):
    if n < 38:
        return n
    else:
        if n%5 > 2:
            return (n+5-n%5)
        else:
            return n
def gradingStudents(grades):
    # Write your code here
    rounded = []
    for grade in grades:
        rounded.append(gradingAlgorithm(grade))
    return rounded