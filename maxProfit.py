prices = [7,1,5,3,6,4]

output = 0
for i in range(len(prices)):
    for j in range(len(prices)):
        if prices[j] - prices[i] > output and j > i:
            output = prices[j] - prices[i]
print(output)