'''
LC141 
'''
# LIst 的爛方法
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        nlst = []
        while True:
            nlst.append(head)
            if head.next == None:
                return False
            head = head.next
            if head in nlst:
                return True
            
            
'''
Two pointer
'''
def hasCycle(self, head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False