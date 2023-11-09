# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead == None:
            return pHead
        result=RandomListNode(pHead.label)
        head=result
        result.next=pHead.next
        result.random=pHead.random
        p=pHead.next
        while p:
            temp=RandomListNode(p.label)
            result.next=temp
            result=temp
            p=p.next
        p=pHead.next
        temp=head.next
        while p:
            if p.random:
                p1=p.random # 标记random
                p2=head # 遍历head
                while p2:
                    if p2.label==p1.label:
                        temp.random=p2
                        break
                    p2=p2.next
            p=p.next
            temp=temp.next
        return head