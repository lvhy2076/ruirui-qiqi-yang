class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


ls1 = [1, 3, 7]
ls2 = [2, 3, 7]
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


def FindFirstCommonNode(pHead1: ListNode, pHead2: ListNode) -> ListNode:
    p1=pHead1
    p2=pHead2
    len1=0
    len2=0
    while p1:
        len1+=1
        p1=p1.next
    while p2:
        len2+=1
        p2=p2.next
    if len1>len2:
        for i in range(len1-len2):
            pHead1=pHead1.next
    else:
        for i in range(len2-len1):
            pHead2=pHead2.next
    while pHead1 and pHead2:
        if pHead1.val==pHead2.val:
            return pHead1
        else:
            pHead1=pHead1.next
            pHead2=pHead2.next
    return None

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
head = FindFirstCommonNode(pHead1, pHead2)

while head:
    print(head.val)
    head = head.next
