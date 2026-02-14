# using math library we will find square root, natural log and Sin  of a number by user input
import math      #importing math module.
number = float(input("Enter a number: "))        # asking for user input
#find square root
sqrt_result = math.sqrt(number)                  #using inbuilt squre root function of math module
#find natural log
log_result = math.log(number)                     #using inbuilt log function of math module
#find sin
sin_result = math.sin(number)                      #using inbuilt sin function of math module
print(f"Square root  is: {sqrt_result}")          #printing value of sqroot, log, sin for different values by user.
print(f"Logarithm {number} is: {log_result}")

print(f"Sin{number} : {sin_result}")
