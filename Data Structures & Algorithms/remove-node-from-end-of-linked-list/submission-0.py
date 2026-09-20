
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        l = dummy
        r = dummy

        for i in range(n+1):
            r = r.next

        while r:
            l = l.next
            r = r.next

        if l and l.next:
            l.next = l.next.next
        else:
            l = None
        # print("l.val:", l.val)
        # print("r.val:", r.val)

        return dummy.next

