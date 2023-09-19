class Solution:
    def majorityelement(self: list[int]) -> int:

        output = 0
        numberCount = 0

        for i in self:
            if self.count(self[i]) > numberCount:
                numberCount = self.count(self[i])
                output = self[i]

        return output

k = Solution.majorityelement([2,2,1,1,1,2,2])
print(k)

