class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = []
        k = 0
        
        for x in range(len(nums)):
            if nums[x] != val:
                res.append(nums[x])
                k += 1
        for i in range(k):
            nums[i] = res[i]
        return k
        