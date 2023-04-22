T = int(input())
for i in range(T):
    s = input()
    odd = ""
    even = ""
    for i in range(len(s)):
        if i%2 == 1:
            odd += s[i]
        else:
            even += s[i]
    print("%s %s"%(even, odd))