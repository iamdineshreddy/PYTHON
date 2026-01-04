def factorial(n):
    """
    Calculates the factorial of a number using a loop.
    """
    if n < 0:
        return None

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Taking input from user
try:
    num = int(input("Enter a number to calculate factorial: "))

    fact = factorial(num)

    if fact is None:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"Factorial of {num} is: {fact}")

except ValueError:
    print("Invalid input! Please enter an integer.")
