class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if len(T) == 1: return [0]
        point = 1
        ans,stack = [0]*len(T),[0]
        while point != len(T):
            if len(stack) == 0 or T[stack[-1]] >= T[point]:
                stack.append(point)
                point +=1
            else:
                ans[stack[-1]] = point - stack[-1]
                stack.pop()
        return ans
