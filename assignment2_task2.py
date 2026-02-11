# finding sum of first n natural numbers using for loop
n=50  #findinding sum of first 50 natural numbers
sum=0       #initializing sum variable
for i in range(1,n+1):   #loop from 1 to n
    sum=sum+i            #adding each number to sum
print(f"The sum of numbers from 1 to {n} is: {sum}")    #printing the sum ,  output will be "The sum of numbers from 1 to 50 is: 1275"
