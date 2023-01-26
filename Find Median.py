def findMedian(arr):
    # Write your code here
    arr.sort()
    len_array = len(arr)
    median = len_array//2
    return arr[median]