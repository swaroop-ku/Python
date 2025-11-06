import matplotlib.pyplot as plt


days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5",
        "Day 6", "Day 7", "Day 8", "Day 9", "Day 10"]

prices = [150, 152, 149, 155, 160, 158, 162, 165, 163, 168]


plt.plot(days, prices, color='green', marker='o', linestyle='-', linewidth=2)


plt.title("Stock Price Over 10 Trading Days")
plt.xlabel("Trading Days")
plt.ylabel("Stock Price (USD)")


plt.show()
