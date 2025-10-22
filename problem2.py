# UNDERSTAND: We need to understand the factorial of a number using a function.
# CLUES: Factorial means multiplying all whole numbers from 1 to that number.
# ASSEMBLE: We'll use a for loop and a variable to store the result.
# SOLVE: Multiply the result by each number in the loop.
# EXAMINE: Test/Input with 5 to see if the output is 120.

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print(factorial(5))
