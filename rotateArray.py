class Solution:
    def rotate(self: list[int], k: int) -> None:

        for i in self[0:-k]:
            self.append(i)
            self.remove(i)
    