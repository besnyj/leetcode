class Solution:
    def dailyTemperatures(self: list[int]) -> list[int]:

        temperatures = self
        output = []
        center, left, right = 0, 0, 0

        while center < len(temperatures):
            if right == len(temperatures):
                output.append(0)
                left += 1
                right = left
                center += 1
            elif temperatures[right] > temperatures[left]:
                diff = right - left
                output.append(diff)
                left += 1
                right = left
                center += 1
            else:
                right += 1

        return output
