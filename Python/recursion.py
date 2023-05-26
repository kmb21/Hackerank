def factorial(n):
    # Write your code here
    if n == 0:
        return 1
    return n * factorial(n-1)
def insert(string, char, n):
    if n <= 0:
        return string
    if len(string) == 1:
        return string
    return string[0] + char*n + insert(string[1:], char, n)

print(insert("cs21", "!", 2))