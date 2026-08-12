class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = set()
        count = 0
        for i in range(len(nums)):
            
            if nums[i] == 1:
                count += 1
            else:
                cnt.add(count)
                count = 0
        cnt.add(count)
        return max(cnt)

