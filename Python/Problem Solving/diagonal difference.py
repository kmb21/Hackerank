# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    leaddiag = 0
    seconddiag = 0
    m = 0
    n = len(arr) - 1
    for i in arr:
        leaddiag += i[m]
        seconddiag += i[n-m]
        m += 1
    return abs(leaddiag-seconddiag)