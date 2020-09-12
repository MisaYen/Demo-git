# -*- coding: utf-8 -*-
"""
Leetcode 234 
Paliandroan Linked list
"""

"""
My Solution
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #print(head.next.val)
        if head == None:
            return True
        arr = []
        while head != None:
            arr.append(head.val)
            head = head.next
        for i in range(len(arr)//2):
            if arr[i] != arr[-i-1]:
                return False
        return True


"""
參考
def isPalindrome(self, head):
    fast = slow = head
    # find the mid node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # reverse the second half
    node = None
    while slow:
        nxt = slow.next
        slow.next = node
        node = slow
        slow = nxt
    # compare the first and second half nodes
    while node: # while node and head:
        if node.val != head.val:
            return False
        node = node.next
        head = head.next
    return True