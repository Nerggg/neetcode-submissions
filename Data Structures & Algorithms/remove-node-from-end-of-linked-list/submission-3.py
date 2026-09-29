
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pointer = dummy
        delete = dummy

        for _ in range(n+1):
            pointer = pointer.next

        while pointer:
            pointer = pointer.next
            delete = delete.next

        delete.next = delete.next.next

        return dummy.next
