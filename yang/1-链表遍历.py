class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def printListFromTailToHead(self, listNode: ListNode) -> list[int]:
        # write code here
        ls = []
        while listNode:
            ls.append(listNode.val)
            listNode = listNode.next
        return ls[::-1]
