# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head.next

        while f and f.next:
            s = s.next
            f = f.next.next

        #reverse of second part
        second = s.next
        prev = s.next =  None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        #merge
        second = prev
        first = head
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2