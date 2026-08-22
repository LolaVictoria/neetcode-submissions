# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        fast = head
        slow = head

       #1. detect middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 2. split into two halves
        second = slow.next
        slow.next = None
        
        #3. reverse from middle
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        second = prev

        
        #reorder
        first = head
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
       


        