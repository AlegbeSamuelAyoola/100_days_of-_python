def factorial(n):
    # Base case
    if n == 1 or n == 0:
        return 1
    else:
        # Recursive call
        return n * factorial(n-1)

# Test the function
print(factorial(5))
