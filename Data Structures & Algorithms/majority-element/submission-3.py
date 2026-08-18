class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = 0
        count = 0
        for i in nums:
            if x == i:
                count += 1
            elif count == 0:
                x = i
                count = 1
            else:
                count -= 1
        return x
        