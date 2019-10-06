class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        arr = []
        for x in range(len(nums)):
            dict[x] = nums[x]
        
        for i in range(len(nums)):
            if (target-dict[i]) in nums and target-dict[i] != dict[i]:
                arr.append(i)
            if target-dict[i] == dict[i] and nums.count(dict[i]) > 1:
                arr.append(i)
            
        return arr
