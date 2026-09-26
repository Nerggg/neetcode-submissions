class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and not list2: return list1
        elif list2 and not list1: return list2

        dummy = ListNode()
        pointer = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                pointer.next = list1
                list1 = list1.next
            else: 
                pointer.next = list2
                list2 = list2.next

            pointer = pointer.next

        if list1:
            pointer.next = list1

        elif list2:
            pointer.next = list2

        return dummy.next






        
