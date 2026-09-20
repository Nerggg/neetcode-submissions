class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        witnessed = {}
        pointer = head
        while pointer:
            if pointer not in witnessed:
                witnessed[pointer] = True
            else:
                return True

            pointer = pointer.next
        return False
        
