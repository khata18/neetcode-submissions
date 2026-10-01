class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for k in range(len(s)):
            countS[s[k]] = 1 + countS.get(s[k], 0)
            countT[t[k]] = 1 + countT.get(t[k], 0)

        return countS == countT