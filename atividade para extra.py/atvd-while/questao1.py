for num in range(1,51):
    if num % 3 == 0:
        print(f"Fizz")
    elif num % 5 == 0:
        print(f"Buzz")
    elif num % 3 == 0 and num % 5 == 0:
        print(f"FizzBuzz,\n")
    else:
        print(num)
