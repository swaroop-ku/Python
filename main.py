# main.py
# Import module
import operations

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum_result = operations.add(num1, num2)
sub_result = operations.subtract(num1, num2)
div_result = operations.divide(num1, num2)
multi_result = operations.multiplication(num1, num2)

print(f"Addition: {sum_result}")
print(f"Subtraction: {sub_result}")
print(f"Divisi0n: {div_result}")
print(f"Multiplication: {multi_result}")