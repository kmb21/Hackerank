def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    appleCount = 0
    orangeCount = 0
    iterate = max(len(apples), len(oranges))
    for i in range(iterate):
        if i < len(apples):
            apples[i] += a
            if apples[i] in range(s, t+1):
                appleCount += 1
        if i < len(oranges):
            oranges[i] += b
            if oranges[i] in range(s, t+1):
                orangeCount += 1
    print(appleCount)
    print(orangeCount)