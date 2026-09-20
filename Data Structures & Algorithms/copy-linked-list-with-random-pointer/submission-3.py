
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
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

            helper = helper.next

        return d[head]

