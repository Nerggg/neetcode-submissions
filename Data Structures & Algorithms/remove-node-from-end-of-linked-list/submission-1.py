class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        delete = dummy
        tape = head

        for _ in range(n):
            tape = tape.next

        while tape:
            delete = delete.next
            tape = tape.next

        delete.next = delete.next.next

        return dummy.next
