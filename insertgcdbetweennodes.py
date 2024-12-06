# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from math import gcd
from typing import Optional


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = head, head.next
        while cur:
            x = gcd(pre.val, cur.val)
            pre.next = ListNode(x, cur)
            pre, cur = cur, cur.next
        return head


head = ListNode(18)
head.next = ListNode(6)
head.next.next = ListNode(10)
head.next.next.next = ListNode(3)
insertGreatestCommonDivisors = Solution().insertGreatestCommonDivisors(head)
print(insertGreatestCommonDivisors)