prices = [29.99, 45.50, 12.75, 38.20]
discount_factor = [10, 20, 15, 5]

updated_prices = prices.copy()

for cost in range(len(prices)):
	updated_prices[cost] -= prices[cost] * (discount_factor[cost] / 100)
	print(f" Updated prices for item {cost}: ${updated_prices[cost]: .2f}")



