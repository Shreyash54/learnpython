''' Reverse Nodes in k-Group
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

code:
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, k):
        prev = None
        curr = head
        while k > 0:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            k -= 1
        return prev

    def reverseKGroup(self, head, k):
        # First, check if there are at least k nodes to reverse
        count = 0
        temp = head
        while temp and count < k:
            temp = temp.next
            count += 1
        
        # If there are fewer than k nodes, return head as is
        if count < k:
            return head
        
        # Reverse the first k nodes
        new_head = self.reverse(head, k)
        
        # After reversing, head will be the last node of the reversed group
        # So we connect it to the result of the next group
        head.next = self.reverseKGroup(temp, k)
        
        return new_head



        
