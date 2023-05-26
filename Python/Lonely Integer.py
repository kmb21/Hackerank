def lonelyinteger(a):
    # Write your code here
    for element in a:
        if a.count(element) < 2:
            return element
