class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)-1):
            seen[nums[i]] = i
            x = target - nums[i+1]
            if x in seen:
                return [seen[x],i+1]