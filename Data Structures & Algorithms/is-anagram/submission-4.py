class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = sorted(list(s))
        b = sorted(list(t))
        if len(s) != len(t):
            return False
        else:
            return a == b