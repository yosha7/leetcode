# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        while len(lists)>1:
            mergedlist=[]
            for i in range (0,len(lists),2):
                l1=lists[i]
                if i+1<len(lists):
                    l2=lists[i+1]
                else:
                    l2=None
                mergedlist.append(self.merge(l1,l2))
            lists=mergedlist
        return lists[0]
    def merge(self,list1,list2):
        dummy=ListNode()
        curr=dummy
        while list1 and list2:
            if list1.val<=list2.val:
                curr.next=list1
                list1=list1.next
            else:
                curr.next=list2
                list2=list2.next
            curr=curr.next
        if list1:
            curr.next=list1
        if list2:
            curr.next=list2
        return dummy.next

        