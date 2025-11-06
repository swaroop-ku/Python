import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]   
y = [40, 50, 60, 70, 80]  


plt.scatter(x, y)

plt.xlabel("Hours Studied")
plt.ylabel("Test Score")
plt.title("Study Time vs Test Score")


plt.show()
