import matplotlib.pyplot as plt


ages = [18, 19, 18, 20, 21, 22, 20, 19, 18, 21, 22, 23, 19, 20, 21, 22, 23, 20, 19, 18]


plt.hist(ages, bins=5, color='lightgreen', edgecolor='black')


plt.xlabel("Age")
plt.ylabel("Number of Students")
plt.title("Age Distribution of Students in a Class")

plt.show()
