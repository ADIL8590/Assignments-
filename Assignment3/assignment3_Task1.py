#FIND FACTORIAL OF A NUMBER USING RECURSION by user input
n=int(input("Enter a number to find its factorial: "))
def factorial(n):     # Defining factorial function
    if n == 0:        # for n=0, set 0!=1
        return 1
    else:             #for n>0, n!=n*(n-1)! recursively
        return n * factorial(n-1)

print(f"The factorial of {n} is: {factorial(n)}")      #printing the value of n!
# Finding factorial of a number using loop by user input
n=int(input("Enter a number to find its factorial: "))
factorial = 1           #inititiate the value of 0!=1
for i in range(1, n+1):     #for i ranging from 1,2,3,...,n-1  n-factorial=n*factorial(n-1), we can also write factorial=factorial*i,   for different i.
    factorial *= i

print(f"The factorial of {n} is: {factorial}")         #printing the value of n!.
