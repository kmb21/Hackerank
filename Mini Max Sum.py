#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sums = []
    for number in arr:
        arr_copy = arr[:]
        arr_copy.remove(number)
        sums.append(sum(arr_copy))
    minimum = min(sums)
    maximum = max(sums)
    print(str(minimum) + " " + str(maximum))
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
