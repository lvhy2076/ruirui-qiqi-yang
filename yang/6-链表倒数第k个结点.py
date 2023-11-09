class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


ls1 = [1, 2, 3]
pHead1 = ListNode(ls1[0])
p1 = pHead1

for i in ls1[1::]:
    temp = ListNode(i)
    pHead1.next = temp
    pHead1 = pHead1.next
pHead1 = p1


def FindKthToTail(pHead: ListNode, k: int):
    p1 = pHead
    p2 = pHead
    for i in range(k):
        if not p2:
            return None
        p2 = p2.next
    while p2:
        p1 = p1.next
        p2 = p2.next
    if p1:
        return p1
while pHead1:
    print(pHead1.val, end=' ')
    pHead1 = pHead1.next
print()
pHead1 = p1
ans = FindKthToTail(pHead1,3)
print(ans.val)
