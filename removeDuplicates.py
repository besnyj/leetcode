class Solution:
    def removeduplicates(self: list[int]) -> int:

        k = 0
        for i in self:
            for j in self:
                if j == i and self[j] != self[i]:
                    self.remove(j)
                    k += 1

        return k, self
#     isn't the best solution because O(nˆ2) and changing the list while iterating it

k = Solution.removeduplicates([0,0,1,1,1,2,2,3,3,4])
print(k)



