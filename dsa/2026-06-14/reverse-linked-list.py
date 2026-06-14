# Reverse Linked List
# Difficulty: Easy
# Date: 2026-06-14
# LeetCode: https://leetcode.com/problems/reverse-linked-list/
# Status: Accepted
# Runtime: 0 ms
# Memory: 20.4 MB

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
