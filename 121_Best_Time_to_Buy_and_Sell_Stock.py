nums = [7,1,5,3,6,4]

min_price = float('inf')
max_profit = 0

for i in nums:
    if i < min_price:
        min_price = i
    profit = i - min_price
    if profit > max_profit:
        max_profit = profit

print("Maximum profit:", max_profit)