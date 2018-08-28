# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ln = [head]
        i = 0
        while ln[i].next:
            ln.append(ln[i].next)
            i += 1
        return ln[len(ln) // 2]
