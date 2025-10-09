n = int(input("Enter the number of terms:"))
x = int(input("Enter the value of cos:"))
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact*i
    return fact

cos_x = 0

for i in range(n):
    term = ((-1) ** i) * (x ** (2 * i)) /factorial(2 * i)
    cos_x += term


print("cos(x) ≈", round(cos_x, 4))