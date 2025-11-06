from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        pre, cur = None, head 
        while cur is not None: 
            if cur.val in nums: 
                if pre == None: 
                    cur = head.next 
                    head = cur
                else: 
                    pre.next = cur.next 
                    cur = cur.next
            else: 
                pre = cur
                cur = cur.next 

        return head
    