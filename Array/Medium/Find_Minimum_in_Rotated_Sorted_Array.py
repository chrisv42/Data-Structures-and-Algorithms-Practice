class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.binSearch(nums)
    
    def binSearch(self, nums: List[int]):
        length = len(nums)
        if length == 1: return nums[0]
        if length == 2: return min(nums)
        mid = (length-1)//2
        if nums[0] < nums[mid] and nums[0] > nums[-1]:
            return self.binSearch(nums[mid:])
        else:
            return self.binSearch(nums[:mid+1])
        
# in array questions that seem too simple.. there is a binary search option probably (check if it's sorted before coming to that conclusion lol)
