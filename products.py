products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

#Average price
average_price = sum(prices) / len(prices)
print(f"Average Price: ${average_price:.2f}")

#New price list with the old reduced by 5
new_prices = [price - 5 for price in prices]
print("New Prices:", new_prices)

#total revenue from the products
total_revenue = sum(price * quantity for price, quantity in zip(prices, last_week))
print(f"Total Revenue: ${total_revenue:.2f}")

#Calculate the average daily revenue generated from the products
average_daily_revenue = total_revenue / sum(last_week)
print(f"Average Daily Revenue: ${average_daily_revenue:.2f}")

#Identify products with prices less than 30 based on the new prices
less_than_30_products = [product for product, price in zip(products, new_prices) if price < 30]
print("Products with prices less than $30:", less_than_30_products)
