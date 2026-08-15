class Solution:
    def isPalindrome(self, s: str) -> bool:
        b = ''.join(c.lower() for c in s if c.isalnum())
        r = len(b) -1
        l = 0
        res = 0
        while l < r:
            if b[r] == b[l]:
                res += 1
            else:
                return False

            r -= 1
            l += 1
        return True
        
                
            
             
            
        