# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        len_list = self.check_len_list(head)
        n_k_group = len_list // k
        residual = len_list % k

        first, last, next_head = self.reverse_group(head, k)

        # remember first first which is head of modified list
        head = first

        for i in range(n_k_group - 1):
            curr_first, curr_last, next_head = self.reverse_group(next_head, k)
            last.next = curr_first
            first = curr_first
            last = curr_last

        last.next = next_head

        return head

    def check_len_list(self, head):
        """
        return the list length
        """
        counter = 1
        curr_node = head
        while True:
            curr_node = curr_node.next
            if curr_node is None:
                return counter
            counter += 1

    def reverse_group(self, head, k):
        """
        reverse nodes and return first and last node of reversed
        current group and head of next group
        head: start node of current group
        """
        prev = None
        curr = head
        last = curr
        for j in range(k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        first = prev
        next_head = curr

        return first, last, next_head
