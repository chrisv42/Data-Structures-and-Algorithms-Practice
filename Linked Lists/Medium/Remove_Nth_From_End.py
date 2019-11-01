# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l = 0
        curr = head
        dummy = ListNode(0) # need this for the edge case that the list is only 1 node long so that it has a curr.next
        dummy.next = head
        while curr:
            curr = curr.next
            l += 1
        l -= n
        curr = dummy
        while l > 0:
            l -= 1 
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next
            
# to remove a node from a linked list, make a dummy linked list that is a copy, set a pointer to = the head, traverse
# until you get to where you need to remove, and to .next = .next.next
