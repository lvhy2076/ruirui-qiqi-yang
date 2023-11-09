class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


ls1 = [1, 2, 3]
ls2 = [4, 5, 6]
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


def merge(pHead1: ListNode, pHead2: ListNode) -> ListNode:
    head = pHead1
    rear = None
    while pHead1:
        rear = pHead1
        pHead1 = pHead1.next
    rear.next = pHead2
    rear2=None
    while pHead2:
        rear2 = pHead2
        pHead2 = pHead2.next
    rear2.next = rear.next
    return head


def EntryNodeOfLoop(pHead: ListNode):
    # write code here
    dt={}
    while pHead:
        if pHead.val in dt:
            return pHead
        else:
            dt[pHead.val] = True
        pHead = pHead.next
    print('null')


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
pHead = merge(pHead1, pHead2)

ans = EntryNodeOfLoop(pHead)
print(ans.val)
