class Solution:
    def removeelement(self: list, val):

        if val not in self: return 0

        nums = self
        val = val

        for i in range(nums.count(val)):
            nums.remove(val)

        expectedNums = nums
        output = len(expectedNums)

        return output, expectedNums


k = (Solution.removeelement([0,1,2,2,3,0,4,2], 2))
print(k)
