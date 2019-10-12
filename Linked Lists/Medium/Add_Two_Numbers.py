class Solution:
    def listtoLinked(self,s1:str):
        assert len(s1) > 0
        if len(s1) == 1: return ListNode(s1[0])
        else:
            node = ListNode(s1[0])
            node.next = self.listtoLinked(s1[1:])
            return node
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ""
        num2 = ""
        while l1 or l2:
            if l1: 
                num1 = num1 + str(l1.val)
                l1 = l1.next
            if l2:
                num2 = num2 + str(l2.val)
                l2 = l2.next
        num1,num2 = num1[::-1],num2[::-1]
        num = int(num1) + int(num2)
        num = str(num)
        num = num[::-1]
        return self.listtoLinked(num)
