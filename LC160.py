'''
LC160 *****
'''

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB :
            return None
        pa = headA
        pb = headB
        while pa != pb:
            pa = headB if pa == None else  pa.next
            pb = headA if pb == None else  pb.next
        
        return pa