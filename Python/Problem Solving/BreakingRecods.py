def breakingRecords(scores):
    # Write your code here
    highbreak = 0
    lowbreak = 0
    l = scores[0]
    h = scores[0]
    for i in range(1, len(scores)):
        if scores[i] > h:
            highbreak += 1
            h = scores[i]
        elif scores[i] < l:
            lowbreak += 1
            l = scores[i]
    return [highbreak, lowbreak]
a = [10,9,8,7,6,5,4,3,2,1]
for i, v in enumerate(a):
    print(i+1, v)