class Solution:
    def addtwonumbers(self: list, list2: list) -> list:

        l1 = ""
        l2 = ""
        output = []

        for i in range(len(self)):
            l1 += str(self[i])

        for j in range(len(list2)):
            l2 += str(list2[j])

        k = str(int(l1)+int(l2))
        for i in k:
            output.append(int(i))
        output.reverse()

        return output

a = Solution.addtwonumbers([2,4,1], [5, 6, 4])
print(a)