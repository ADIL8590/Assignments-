# using math library we will find square root, natural log and Sin  of a number by user input
import math
number = float(input("Enter a number: "))
#find square root
sqrt_result = math.sqrt(number)
#find natural log
log_result = math.log(number)
#find sin
sin_result = math.sin(number)
print(f"Square root  is: {sqrt_result}")
print(f"Logarithm {number} is: {log_result}")
print(f"Sine {number} : {sin_result}")