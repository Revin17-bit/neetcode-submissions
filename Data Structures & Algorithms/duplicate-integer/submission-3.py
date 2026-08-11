class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        b = set(nums)
        if len(nums) == len(b)  :
            return False
        return True