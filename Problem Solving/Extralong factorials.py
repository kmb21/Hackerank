def extraLongFactorials(n):
    # Write your code here
    if n <= 1:
        return 1
    else:
        #print(n)
        ans = n * extraLongFactorials(n-1)
        return ans