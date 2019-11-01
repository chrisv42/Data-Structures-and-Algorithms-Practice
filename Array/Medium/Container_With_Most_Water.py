class Solution:
    def maxArea(self, height: List[int]) -> int:
        globalMax = 0
        L = 0
        R = len(height)-1
        while L != R:
            a = (R-L)*min(height[R],height[L])
            if a > globalMax:
                globalMax = a
            if height[R] > height[L]:
                L += 1
            else:
                R -= 1
        return globalMax
