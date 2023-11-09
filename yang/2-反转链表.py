class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def ReverseList(self, head: ListNode) -> ListNode:
    # write code here
    lt_head = ListNode
    while head:
        lt = ListNode
        if lt_head:  # 链表不为空
            lt.val = head.val
            lt_head.next = lt
        else:  # 链表为空
            lt_head.val = head.val
            lt_head.next = None
        head = head.next


lt = ListNode(1)
head = lt
for i in range(5):
    x=input()
    temp = ListNode(x)
    lt.next = temp
lt = head
while lt:
    print(lt.val)
    lt = lt.next
