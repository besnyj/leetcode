class Solution:
    def dailyTemperatures(self: list[int]) -> list[int]:

        temperatures = self
        output = []
        c, l, r = 0, 0, 0

        while c < len(temperatures):
            if r == len(temperatures):
                output.append(0)
                l += 1
                r = l
                c += 1
            elif temperatures[r] > temperatures[l]:
                diff = r - l
                output.append(diff)
                l += 1
                r = l
                c += 1
            else:
                r += 1

        return output
