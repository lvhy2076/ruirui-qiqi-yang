class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


ls1 = [1, 3, 7]
ls2 = [2, 4, 5, 6, 8, 9]
pHead1 = ListNode(ls1[0])
p1 = pHead1

for i in ls1[1::]:
    temp = ListNode(i)
    pHead1.next = temp
    pHead1 = pHead1.next

pHead2 = ListNode(ls2[0])
p2 = pHead2
for i in ls2[1::]:
    temp = ListNode(i)
    pHead2.next = temp
    pHead2 = pHead2.next
pHead1 = p1
pHead2 = p2


def Merge(pHead1: ListNode, pHead2: ListNode) -> ListNode:
    if not pHead1:
        return pHead2
    if not pHead2:
        return pHead1
    if pHead1.val > pHead2.val:
        pHead1, pHead2 = pHead2, pHead1
    head = pHead1
    while pHead1.next and pHead2:
        p = pHead2.next
        if pHead1.next.val > pHead2.val:
            pHead2.next = pHead1.next
            pHead1.next = pHead2
            pHead2 = p
        else:
            pHead1 = pHead1.next
    if not pHead1.next:
        pHead1.next = pHead2
    return head


while pHead1:
    print(pHead1.val, end=' ')
    pHead1 = pHead1.next
print()
while pHead2:
    print(pHead2.val, end=' ')
    pHead2 = pHead2.next
print()
pHead1 = p1
pHead2 = p2
head = Merge(pHead1, pHead2)

while head:
    print(head.val)
    head = head.next
