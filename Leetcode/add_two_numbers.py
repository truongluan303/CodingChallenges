from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num_str1 = ""
        num_str2 = ""
        
        cur1 = l1
        cur2 = l2
        
        while cur1 is not None:
            num_str1 += str(cur1.val)
            cur1 = cur1.next
            
        while cur2 is not None:
            num_str2 += str(cur2.val)
            cur2 = cur2.next
            
        num1 = int(num_str1[::-1])
        num2 = int(num_str2[::-1])
        total = str(num1 + num2)
        
        print(num1, num2, total)
        
        head = ListNode(int(total[-1]))
        cur = head
        for i in range(len(total) - 2, -1, -1):
            c = total[i]
            cur.next = ListNode(int(c))
            cur = cur.next
            
        return head