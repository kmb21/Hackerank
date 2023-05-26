def plusMinus(arr):
    # Write your code here
    plus = 0
    minus = 0
    zero = 0
    n = len(arr)
    for i in arr:
        if i > 0:
            plus += 1
        elif i<0:
            minus += 1
        else:
            zero += 1
    print("%.6f"%(plus/n))
    print("%.6f"%(minus/n))
    print("%.6f"%(zero/n))