
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif list1 and not list2:
            return list1
        elif not list1 and list2:
            return list2

        if list1.val <= list2.val:
            result_head = ListNode(list1.val)
            list1 = list1.next
        else:
            result_head = ListNode(list2.val)
            list2 = list2.next

        pointer = result_head

        while list1 or list2:
            # print("temporary result:")
            # printLinkedList(result_head)
            # print("temporary list1:")
            # printLinkedList(list1)
            # print("temporary list2:")
            # printLinkedList(list2)
            # print()
            if list1 and list2:
                if list1.val <= list2.val:
                    pointer.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    pointer.next = ListNode(list2.val)
                    list2 = list2.next

                pointer = pointer.next

            elif list1 or list2:
                if list1:
                    pointer.next = ListNode(list1.val)
                    list1 = list1.next

                if list2:
                    pointer.next = ListNode(list2.val)
                    list2 = list2.next

                pointer = pointer.next

        return result_head
        
