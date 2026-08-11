class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = list(s)
        b = list(t)
        a.sort()
        b.sort()
        if len(s) != len(t):
            return False
        else:
            return a == b