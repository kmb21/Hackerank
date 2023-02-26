def diagonalDifference(arr):
    i = len(arr)-1
    j = 0
    n = len(arr)
    firstdiag = 0
    leadingdiag = 0
    while i >= 0:
        firstdiag += arr[i][i]
        leadingdiag += arr[i][j]
        i -= 1
        j+=1
        
    if firstdiag > leadingdiag:
        return firstdiag-leadingdiag
    else:
        return leadingdiag-firstdiag