def sum(a,b):
    return a+b

def diff(a,b):
    return a-b

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
print("Addition:",sum(num1,num2))
print("subtraction:",diff(num1,num2))

power = lambda a : a**2
print("Square:",power(num1))

div = lambda x,y: x//y
print("Div:",div(num1,num2))