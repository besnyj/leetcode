class Solution:
    def strStr(haystack: str, needle: str) -> int:

        n=0
        i=0
        j=0
        for letter in haystack[0+n:len(needle)]:
            if j == len(needle):
                n+=1
                i=0
                j=0
            if letter == needle[i]:
                i=+1
            if i == len(needle):
                return 10
            else:
                j+=1

        print(i)


print(Solution.strStr("suckbutsad", "sad"))