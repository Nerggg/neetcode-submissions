
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        single_pointer = head
        double_pointer = head

        while single_pointer and double_pointer:
            try:
                single_pointer = single_pointer.next
                double_pointer = double_pointer.next.next
            except:
                break
            if single_pointer == double_pointer: return True
        return False
        
