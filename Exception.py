try:
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    ans = num1//num2
    print("Division:",ans)
except ZeroDivisionError:
    print("Your denominator is zero")
except ValueError:
    print("ValueError Found")
else:
    print("Division sucessfully")
finally:
    print("You are at the end")