with open("example.txt",'w') as file:
    file.write("My name is swaroop\n")
    file.write("I am student of CSE\n")

#appending
with open("example.txt",'a') as file:
    file.write("I am learning python")
    
#reading file
with open("example.txt",'r') as file:
    s = file.read()
    print(s)
    file.close()
