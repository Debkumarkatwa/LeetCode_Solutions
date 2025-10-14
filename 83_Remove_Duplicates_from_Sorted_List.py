# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head
    

a = Solution()
head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
print(a.deleteDuplicates(head))

h2 = ListNode(1, ListNode(1, ListNode(1)))
print(a.deleteDuplicates(h2))