def birthday(s, d, m):
    # Write your code here
    possibilities = 0

    for number in range(len(s)):
        summation = s[number]
        b = number+1
        while b<m+number and b<len(s):
            summation += s[b]
            b+=1
        if summation == d:
            possibilities += 1
    return possibilities
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
