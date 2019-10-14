class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalMax = localMax = nums[0]
        for x in nums[1:]:
            localMax = max(x, localMax + x)
            globalMax = max(globalMax, localMax)
        return globalMax
