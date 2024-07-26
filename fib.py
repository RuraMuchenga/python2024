def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


try:
    n = int(input("Enter a positive integer: "))
    if n <= 0:
        print("Input should be a positive integer.")
    else:
        print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
except ValueError:
    print("Invalid input. Please enter a positive integer.")
