import matplotlib.pyplot as plt

products = ["A", "B", "C", "D", "E"]
sales = [150, 200, 120, 300, 250]


plt.bar(products, sales, color='skyblue', width=0.5)  # try 0.3 or 0.8 to see the difference

plt.title("Product Sales with Custom Bar Width")
plt.xlabel("Products")
plt.ylabel("Sales (Units)")
plt.show()
