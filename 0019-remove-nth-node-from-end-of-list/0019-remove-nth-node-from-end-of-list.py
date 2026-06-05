# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        count=0
        curr=head
        while curr:
            curr=curr.next
            count+=1
        if n==count:
            return head.next

        target=count-n
        temp=head
        for i in range(target-1):
            temp=temp.next
        temp.next=temp.next.next
        return head
        

        