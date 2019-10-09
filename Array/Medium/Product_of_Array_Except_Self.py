class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rev = nums[::-1]
        prod = [1,nums[0]]
        revprod = [1,rev[0]]
        res = []
        
        for i in range(2,len(nums)):
            prod.append(prod[i-1]*nums[i-1])
            revprod.append(revprod[i-1]*rev[i-1])
        
        for x in range(len(nums)):
            res.append(prod[x]*revprod[len(revprod)-1-x])
            
        return res
