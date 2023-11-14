class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


ls1 = [1, 1, 2]
pHead1 = ListNode(ls1[0])
p1 = pHead1

for i in ls1[1::]:
    temp = ListNode(i)
    pHead1.next = temp
    pHead1 = pHead1.next
pHead1 = p1


def deleteNode(head: ListNode, val: int):
    if not head:
        return head
    # 检测第一个结点
    while head and head.val == val:
        head = head.next
    if not head:
        return head
    pre = head
    p = pre.next
    while p:
        if p.val == val:
            pre.next = p.next
        else:
            pre = pre.next
        p = p.next
    return head


while pHead1:
    print(pHead1.val, end=' ')
    pHead1 = pHead1.next
print()
pHead1 = p1
ans = deleteNode(pHead1, 1)
while ans:
    print(ans.val, end=' ')
    ans = ans.next
print()
