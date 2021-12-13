from typing import Optional,List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def tailInsert(self, val):
        p = self
        while p.next != None:
            p = p.next
        node = ListNode(val)
        p.next = node

    def traverse(self):
        p = self
        while p != None:
            print(p.val, end="->")
            p = p.next


def createLinkedList(numbers):
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dic={}
        for num in nums:
            dic[num]=True
        while head.val in dic:
            head = head.next
        p1,p2=head,head.next
        while p2!=None:
            while p2.val in dic:
                p2=p2.next
                p1.next=p2
                if not p2:
                    return head
            p1=p1.next
            if not p1:
                return head
            p2=p1.next
        return head

if __name__ == '__main__':
    head = [3,7,1,8,1]
    head = createLinkedList(head)
    s = Solution()
    ll=s.modifiedList([1,7,6,2,4],head)
    ll.traverse()
