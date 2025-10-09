import array
num = array.array('i',[1,2,3,4,5])
print(num)
print(type(num))
print("First element is",num[0])
num.append(7)
num.pop()
print(num)

print(num.index(3)) #finding index of element
num.reverse()
print(num)