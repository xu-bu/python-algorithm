import bisect
from collections import *
from functools import *
from heapq import *
import itertools
from heapq import *
from math import *
import string
from decimal import Decimal
from math import gcd
from sortedcontainers import SortedList
from typing import List, Union, Optional
import random
import copy
class TreeNode:
    val = 0
    left, right = None, None

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left, self.right = left, right


# 通过root遍历一棵树，初始队列只有根节点，count从0开始递增，每次将queue[count].val加入到输出中，同时将被遍历的节点的孩子节点全部加入到queue中，如果遍历到空节点，则向输出中加入null，直到count==len(queue)
def TreeNodeToString(root) -> string:
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    # -2是因为逗号后面还有空格
    return "[" + output[:-2] + "]"


# 对列表中的每个根节点进行TreeNodeToString
def TreeNodeArrayToString(TreeNodeArray):
    serializedTreeNodes = []
    for TreeNode in TreeNodeArray:
        serializedTreeNode = TreeNodeToString(TreeNode)
        serializedTreeNodes.append(serializedTreeNode)
    return "[{}]".format(', '.join(serializedTreeNodes))


def inputToTreeNode(input) -> TreeNode:
    if type(input) == str:
        input = input.strip()
        # input = input[1:-1]
        if not input:
            return None

        inputValues = [s.strip() for s in input.split(',')]
    elif type(input) == list:
        inputValues = input
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

class Solution:
    # 95
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        # 根据[start,end]中的数生成所有可行的bst,返回存有这些bst的根节点的列表
        def generate(start, end):
            if start > end:
                # 返回空节点，在start==end的情况，根节点的孩子节点就是两个这样的空节点
                return [None]
            # 每一次generate可行bst列表的时候，[start,end]都不同，所以需要重置ans
            ans = []
            for i in range(start, end + 1):
                # 根节点为i的时候，生成左右子树列表
                leftTrees = generate(start, i - 1)
                rightTrees = generate(i + 1, end)
                for l in leftTrees:
                    for r in rightTrees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        ans.append(root)
            return ans

        return generate(1, n) if n else []

    # 上一题的dp做法，把哈希表当作二维数组，存储build(start,end)的结果以供重复使用。dp[start*n+end]=build(start,end)
    def generateTreesDP(self, n):
        dp = collections.defaultdict(list)

        def build(start, end):
            if start > end:
                return [None]
            elif start == end:
                return [TreeNode(start)]
            for i in range(start, end + 1):
                if len(dp[n * start + i - 1]) != 0:
                    leftTrees = dp[n * start + i - 1][:]
                else:
                    leftTrees = build(start, i - 1)
                if len(dp[(i + 1) * n + end]) != 0:
                    rightTrees = dp[(i + 1) * n + end][:]
                else:
                    rightTrees = build(i + 1, end)
                for left in leftTrees:
                    for right in rightTrees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        dp[start * n + end].append(root)
            return dp[start * n + end]

        return build(1, n)
    
    # 105 根据前序遍历和中序遍历恢复二叉树
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        dic = {}
        # 利用字典，快速确定preorder中根节点的index
        for i in range(len(inorder)):
            dic[inorder[i]] = i

        def myBuild(preStart, preEnd, inStart, inEnd):
            if inStart == inEnd:
                return None
            elif inStart + 1 == inEnd:
                return TreeNode(preorder[preStart])
            root = TreeNode(preorder[preStart])
            inOrderMidIndex = dic[preorder[preStart]]
            leftLen = inOrderMidIndex - inStart
            rightLen = inEnd - inOrderMidIndex - 1
            l = myBuild(preStart + 1, preStart + leftLen + 1, inStart, inStart + leftLen)
            r = myBuild(preStart + leftLen + 1, preStart + leftLen + 1 + rightLen, inOrderMidIndex + 1, inEnd)
            root.left = l
            root.right = r
            return root

        return myBuild(0, len(preorder), 0, len(inorder))

if __name__ == '__main__':
    edges = [[0, 1], [1, 2], [2, 3]]
    coins = [10, 10, 3, 3]
    k = 5
    root = [5,4,8,11,'null',13,4,7,2,'null','null',5,1]
    s = Solution()
    root = inputToTreeNode(root)
    print(s.pathTarget(root, 22))
