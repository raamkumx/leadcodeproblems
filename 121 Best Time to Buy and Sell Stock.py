# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the
# future to sell that stock.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5

# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0

prices = [7, 6, 4, 3, 1]
buy_day = prices[0]
profit = 0

for price in prices[1:]:
    if price < buy_day:
        buy_day = price
    else:
        prob_profit = price - buy_day
        profit = max(profit, prob_profit)

print(profit)
