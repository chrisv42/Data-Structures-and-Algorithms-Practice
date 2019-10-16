class Solution:
    def hasCycle(self, head: ListNode) -> bool:
    
        fast = slow = head
            
        if not head:
            return False
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
