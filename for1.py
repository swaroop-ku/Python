#for loop 

#Program 1)
# n = int(input("Enter the number:"))
# for i in range(1,n+1):
#     print(i)


#Program 2)
# n = int(input("Enter the number:"))
# for i in range(2,n+2,2):
#     print(i)

#Program 3)
# n = int(input("Enter the number:"))
# for i in range(1,n+2,2):
#     print(i)

#Program 4)
# n = int(input("Enter the number:"))
# for i in range(n):
#     print(2**i,end=" ")


#program 5)
# n = int(input("Enter the number:"))
# def factorial(num):
#     fact = 1
#     for i in range(1,num+1):
#         fact = fact*i
#     return fact
# total = 0
# for i in range(1,n+1):
#     total += 1/factorial(i)
# print(round(total+1,2))


#program 6)
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



#program 7)
# n = int(input("Enter the number:"))
# sq = round(pow(n,0.5))
# flag = 0
# for i in range(2,sq):
#     if sq%2 == 0:
#         flag = 1
# if flag == 0:
#     print("Square root of a given number is a prime")
# else:
#     print("Square root of a given number is not prime")



#Program 8)
# for i in range(3):
#     print("A B C")


#Program 9)
# n = int(input("Enter the number:"))
# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+j),end=" ")
#     print()


#Program 10)
# n = int(input("Enter the number:"))
# for i in range(n):
#     for j in range(n-i):
#         print(chr(65+j),end=" ")
#     print()


#Program 11)
# n = int(input("Enter the number:"))
# for i in range(n):
#     for j in range(1,i+2):
#         print(j,end=" ")
#     print()


#Program 12)
# n = int(input("Enter the number:"))
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end=" ")
#     print()