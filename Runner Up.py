if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    array = list(arr)
    array.sort()
    biggest = array[len(array)-1]
    runner = array[0]
    for number in array:
        if number != biggest and number > runner:
            runner = number
    print(runner)