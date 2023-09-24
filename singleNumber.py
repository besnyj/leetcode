nums = [4,1,2,1,2]

numss = 0
for i in nums:
    if nums.count(i) == 1:
        numss = i

print(numss)