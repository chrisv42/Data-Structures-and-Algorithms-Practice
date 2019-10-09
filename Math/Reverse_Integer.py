class Solution:
    def reverse(self, x: int) -> int:

        if x < 0:
            temp = x*-1
        else:
            temp = x
        numString = str(temp)
        numList = list(numString)
        reverseList = []
        
        for i in range(len(numList)-1, -1,-1):
            reverseList.append(numList[i])

        reverseString = ''.join(reverseList)
        reverseInt = int(reverseString)
        if x < 0:
            reverseInt = reverseInt*-1
        if (reverseInt > ((2 ** 31)-1) or reverseInt < (-2 ** 31)):
            return 0
        return reverseInt
