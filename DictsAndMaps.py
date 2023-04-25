n = int(input())
d = {}
for i in range(n):
    data = input()
    temp = data.split()
    d[temp[0]] = temp[1]
while True:
    try:
        query = input().strip()
    except EOFError:
        break
    if query in d:
        print("%s=%s"%(query,d[query]))
    else:
        print("Not found")