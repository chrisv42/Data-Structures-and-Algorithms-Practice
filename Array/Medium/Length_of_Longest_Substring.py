class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        count = L = R = 0
        while len(s) > L and len(s) > R:
            if s[R] in dic:
                dic.pop(s[L])
                L += 1
            else:
                dic[s[R]] = 0
                R+=1
                count = max(count, R-L)
        return count       
