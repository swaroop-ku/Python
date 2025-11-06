import matplotlib.pyplot as plt
brands = ["Samsung", "Apple", "Xiaomi", "OnePlus", "Others"]
market_share = [30, 25, 20, 15, 10]
plt.pie(market_share, labels=brands, autopct="%1.1f%%")
plt.title("Market Share of Mobile Phone Brands")
plt.show()
