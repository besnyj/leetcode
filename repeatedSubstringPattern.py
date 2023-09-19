class Solution:
    def repeated(self: str) -> bool:
        if len(self) % 2 != 0: return False

        n = 0
        i = 0
        for k in range(len(self)):
            if self[i:i+2].find(self[0:2]) != -1:
                n+=1
                i+=1
            if n == 2:
                return True
            else:
                i+=1
        return False



print(Solution.repeated("abacabab"))