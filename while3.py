#While - Above average - 1)
# n = int(input("Enter the number:"))
# flag = 0
# i=2
# while i < n:
#      if n%i == 0:
#         flag = 1
#      i = i+1
# if flag == 0:
#     print("Number is prime")
# else:
#     print("Number is not prime")


#While - Above average - 2)
# n = int(input("Enter the number:"))
# sum = 0
# while n != 0:
#    rem = n%10
#    sum = sum + rem
#    n = n//10
# print("Sum:",int(sum))


#While - Above average - 3)
# n = int(input("Enter the number:"))
# x = n
# m = 0
# while n!= 0:
#     rem = n%10
#     m = m*10 + rem
#     n = n // 10
# if x == m:
#     print("Number entered is a palindrome")
# else:
#     print("Number entered is not a palindrome")


#While - Above average - 4)
n = int(input("Enter the number:"))
m = 0
while n!= 0:
    rem = n%10
    m = m*10 + rem
    n = n // 10
print("Reversed number is",m)