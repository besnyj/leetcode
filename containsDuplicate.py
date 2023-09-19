class Solution:
    def containsduplicate(self: list[int]) -> bool:

        for numbers in self:
            if self.count(numbers) > 1:
                return True
        return False


k = Solution.containsduplicate([2,14,18,22,22])
print(k)