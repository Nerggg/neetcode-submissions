class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        single_pointer = head
        double_pointer = head

        while double_pointer and double_pointer.next:
            single_pointer = single_pointer.next
            double_pointer = double_pointer.next.next
            if single_pointer == double_pointer: return True
        return False
        
