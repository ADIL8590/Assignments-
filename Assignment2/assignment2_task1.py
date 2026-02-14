#To check if a number is even or odd
num=int(input("Enter a number : "))  #taking input from user
if num%2==0:    #checking if number is divisible by 2
    print(f"{num} is an even number.")   #printing if number is even
else:
    print(f"{num} is an odd number.")    #printing if number is odd
