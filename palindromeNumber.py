class Solution:
    def isPalindrome(self):
        number = str(self)

        reversedNumber = ""
        for i in number:
            reversedNumber = f'{i}{reversedNumber}'
        return reversedNumber == number

print(Solution.isPalindrome(1001))