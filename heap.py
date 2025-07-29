import bisect
import collections
import heapq
import string

#涉及到一串数组慢慢输入，求过程中最值的问题，可以考虑堆排序
#如果在海量数据中找出最大的100个数字，就适用于堆排序，因为如果数据量很大，使用其他的排序方法可能导致一个机器的内存不足以一次读取这么多数据
class Heap:
    def __init__(self,nums):
        self.heap=nums
        
    def heappush(self, item):
        """Push item onto heap, maintaining the heap invariant."""
        self.heap.append(item)
        #自底向上调整，不断地和父节点比较
        self.siftdown(0, len(self.heap) - 1)

    def heappop(self):
        """Pop the smallest item off the heap, maintaining the heap invariant."""
        lastelt = self.heap.pop()  # raises appropriate IndexError if heap is empty
        if self.heap:
            returnitem = self.heap[0]
            #把根节点换成数组中的最后一个元素
            self.heap[0] = lastelt
            #从0位置开始自顶向下调整，使整棵树满足最小堆规范
            self.siftup(0)
            return returnitem
        return lastelt

    #使用heapify比一个一个地heappush效率高
    def heapify(self):
        """Transform list into a heap, in-place, in O(len(x)) time."""
        n = len(self.heap)
        #从底层的一半数开始调整，调整一半就够了
        for i in reversed(range(n // 2)):
            self.siftup(i)

    def siftdown(self, startpos, pos):
        newitem = self.heap[pos]
        # Follow the path to the root, moving parents down until finding a place
        # newitem fits.
        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parent = self.heap[parentpos]
            if newitem < parent:
                self.heap[pos] = parent
                pos = parentpos
                continue
            break
        self.heap[pos] = newitem

    def siftup(self, pos):
        endpos = len(self.heap)
        startpos = pos
        newitem = self.heap[pos]
        # Bubble up the smaller child until hitting a leaf.
        childpos = 2 * pos + 1  # leftmost child position
        while childpos < endpos:
            # Set childpos to index of smaller child.
            rightpos = childpos + 1
            if rightpos < endpos and not self.heap[childpos] < self.heap[rightpos]:
                childpos = rightpos
            # Move the smaller child up.
            self.heap[pos] = self.heap[childpos]
            pos = childpos
            childpos = 2 * pos + 1
        # The leaf at pos is empty now.  Put newitem there, and bubble it up
        # to its final resting place (by sifting its parents down).
        self.heap[pos] = newitem
        #不是很懂这里为什么还要再上浮一遍
        self.siftdown(startpos, pos)
        
class ListNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
    def traverse(self):
        p = self
        while p != None:
            print(p.val,end="->")
            p = p.next

class Solution:
    #23 优先队列处理链表
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        dummy = ListNode(0)
        p = dummy
        while heap:
            val, index = heapq.heappop(heap)
            p.next = ListNode(val)
            p = p.next
            if lists[index].next:
                lists[index] = lists[index].next
                heapq.heappush(heap, (lists[index].val, index))
        return dummy.next

    #373
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heap=[]
        #固定第一个元素是第一个数组中最小的数，遍历第二个数组，构造可能的最小数对
        for each in [[0,i]for i in range(min(len(nums2),k))]:
            heapq.heappush(heap,(nums1[each[0]]+nums2[each[1]],each[0],each[1]))
        ans=[]
        #弹出k次，每次都是弹出的最小的
        while k>0 and len(heap)>0:
            val,index1,index2=heapq.heappop(heap)
            ans.append([nums1[index1],nums2[index2]])
            #弹出最小的index1,index2之后，由于index2是被遍历过的，所以只用变index1，下一个可行的索引只能是index1+1,index2
            if index1+1<len(nums1):
                heapq.heappush(heap, (nums1[index1+1]+nums2[index2],index1+1 , index2))
            k-=1
        return ans

if __name__ == '__main__':
    nums=[3,324,6,8,0,9]
    solution=Solution()
    print(solution.findKthLargest(nums,4))
    heap=Heap(nums)
    heap.heapify()
    print(heap.heap)
