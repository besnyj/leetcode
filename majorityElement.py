def majorityElement(self: list[int]) -> int:
        output = 0
        numberCount = 0
        countedNumbers = []
        for i in self:
            if self.count(i) > numberCount and i not in countedNumbers:
                numberCount = self.count(i)
                output = i
            else:
                countedNumbers.append(i)

        print(countedNumbers)

majorityElement([])