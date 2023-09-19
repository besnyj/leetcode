class Solution:
    def canplaceflowers(self: list[int], n:int) -> bool:

        e = 0

        if len(self) <= 2 or n == 0:
            e = 1
            return e >= 1
        if self[0] == 0 and self[0+1] == 0:
            self[0] = 1
            e += 1
        if self[-1] == 0 and self[-2] == 0:
            self[-1] = 1
            e += 1
        for i in range(len(self)):
            if self[i] == 0 and self[i+1] == 0 and self[i-1] == 0:
                e += 1
        return e >= n


k = Solution.canplaceflowers([0], 0)
print(k)
