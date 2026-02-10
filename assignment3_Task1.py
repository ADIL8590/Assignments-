#FIND FACTORIAL OF A NUMBER USING RECURSION by user input
n=int(input("Enter a number to find its factorial: "))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(f"The factorial of {n} is: {factorial(n)}")
# Finding factorial of a number using loop by user input
n=int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(1, n+1):
    factorial *= i
print(f"The factorial of {n} is: {factorial}")