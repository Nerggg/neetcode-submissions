
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        front = head
        back = head
        prev_of_back = None
        next_of_front = front.next
        total_len = 0
        curr_len = 0
        while back.next:
            prev_of_back = back
            back = back.next
            total_len += 1

        while curr_len < total_len:
            # inserting 0 -> 6 -> 1
            front.next = back
            curr_len += 1
            if curr_len == total_len: break

            front = front.next

            front.next = next_of_front
            curr_len += 1
            if curr_len == total_len: break

            front = front.next

            # advancing 1 to 2
            next_of_front = next_of_front.next

            # step back the "back" from 6 to 5
            back = prev_of_back

            # step back the "prev_of_back" from 5 to 4
            prev_of_back = next_of_front
            while prev_of_back.next != back:
                prev_of_back = prev_of_back.next
                # print("prev_of_back.val:", prev_of_back.val)
                # print("disini?")

            # now at this point front points at 1 in 0 -> 6 -> 1
            # now we can repeat the whole thing with while loop
            # print("curr_len:", curr_len)

        if front and front.next:
            front.next.next = None

        return None

