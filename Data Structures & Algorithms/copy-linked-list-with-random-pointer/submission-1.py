
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        dummy = Node(0)
        pointer = dummy.next
        helper = head
        d = {}

        while helper:
            d[helper] = Node(helper.val)
            helper = helper.next

        helper = head
        while helper:
            if helper.next:
                d[helper].next = d[helper.next]
            if helper.random:
                d[helper].random = d[helper.random]

            pointer = d[helper]

            # print("pointer.val:", pointer.val)
            # print("pointer.next:", pointer.next)
            # print("pointer.random:", pointer.random)

            pointer = pointer.next
            helper = helper.next

        return d[head]

