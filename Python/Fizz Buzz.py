def fizzBuzz(n):
    # Write your code here
    for number in range(1,n+1):
        mod3 = number%3
        mod5 = number%5
        if mod3==0 and mod5==0:
            print("FizzBuzz")
        elif mod3==0 and mod5!=0:
            print("Fizz")
        elif mod5==0 and mod3!=0:
            print("Buzz")
        else:
            print(number)