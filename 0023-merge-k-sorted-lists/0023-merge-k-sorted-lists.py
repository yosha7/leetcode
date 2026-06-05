class Solution(object):
    def mergeKLists(self, lists):

        if not lists:
            return None

        head = None

        for l in lists:
            head = self.merge(head, l)

        return head

    def merge(self, list1, list2):

        dummy = ListNode()
        curr = dummy

        while list1 and list2:

            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        if list1:
            curr.next = list1

        if list2:
            curr.next = list2

        return dummy.next