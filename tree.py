import collections
from queue import Queue
from typing import Optional, List
import string
from itertools import chain


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


# 递归层次遍历
def visitLevel(head: TreeNode, level):
    if head == None:
        return
    elif level == 1:
        print(head.val)
    else:
        visitLevel(head.left, level - 1)
        visitLevel(head.right, level - 1)


def countHeight(head: TreeNode):
    if head == None:
        return 0
    else:
        left = countHeight(head.left)
        right = countHeight(head.right)
        return max(left, right) + 1


def countNode(head):
    if head == None:
        return 0
    else:
        return countNode(head.left) + countNode(head.right) + 1


def isFullBtree(head: TreeNode):
    if pow(2, countHeight(head)) - 1 == countNode(head):
        return True
    else:
        return False


# 层次遍历二叉树的节点（包括空节点），全部放到一个队列里，会发现以下规律：
#
# A B C D E F G 0 0 0 0 0 0
#
# 规律就是前面是非空节点，而后面是空节点。如果是非完全二叉树呢，那么出现以下现象：
#
# A B 0 0 C D 0 0 E F G
# 所以只需要不管孩子节点是不是空节点，都入队，直到遇到空节点出队时，将所有节点出队，如果还有非空节点则说明不是完全二叉树
def isCompleteTree(head: TreeNode):
    if head == None:
        return True
    else:
        q = Queue()
        q.put(head)

        while (p := q.get()):
            q.put(p.left)
            q.put(p.right)
        while (not q.empty()):
            p = q.get()
            if (p != None):
                return False
        return True


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

    # 98 bst的中序遍历序列一定是递增的
    def isValidBST(self, root: TreeNode) -> bool:
        ans = []

        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            ans.append(root.val)
            inOrder(root.right)

        inOrder(root)
        i = 1
        while i < len(ans):
            if ans[i] <= ans[i - 1]:
                return False
        return True

    # 102
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        item = []
        ans = []
        index, cur, next, count, size = 0, 1, 0, 0, 1
        while index < size:
            node = queue[index]
            item.append(node.val)
            count += 1
            if node.left:
                queue.append(node.left)
                next += 1
                size += 1
            if node.right:
                queue.append(node.right)
                next += 1
                size += 1
            # 这一步判断必须在循环的最后
            if count == cur:
                ans.append(item[:])
                item = []
                cur, next, count = next, 0, 0
            index += 1
        return ans

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

    # 113 dfs遍历二叉树的所有路径
    # 只不过是在前序遍历上加上了一个判断（访问叶子节点时把items放到ans中）和一个pop（）
    # 然后有target的处理
    def pathSum(self, root: [TreeNode], targetSum: int) -> list[list[int]]:
        ans = []
        items = []

        def dfs(node, items, target):
            if not node:
                return
            # visit部分
            items.append(node.val)
            # target是形参，能够隐形回溯，所以之后不用回溯target
            target -= node.val
            if not node.left and not node.right:
                if target == 0:
                    ans.append(items[:])

            dfs(node.left, items, target)
            dfs(node.right, items, target)
            # 多加一个回溯
            items.pop()

        dfs(root, items, targetSum)
        return ans

    # 236 二叉树中找任意两个节点的最近公共祖先
    # 首先遍历树，生成字典存储节点与其父节点的对应关系，然后从p节点出发去寻找根节点，标记路过的节点，最后从q节点出发回到根节点，当发现第一个被标记了的父节点时，即为ans
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        dic = {}

        def preOrder(root):
            if not root:
                return
            if root.left:
                dic[root.left.val] = root
                preOrder(root.left)
            if root.right:
                dic[root.right.val] = root
                preOrder(root.right)

        preOrder(root)
        visit = collections.defaultdict(int)
        while p != root:
            visit[p.val] = 1
            p = dic[p.val]
        visit[p.val] = 1
        while visit[q.val] != 1:
            q = dic[q.val]
        return q


if __name__ == '__main__':
    edges = [[0, 1], [1, 2], [2, 3]]
    coins = [10, 10, 3, 3]
    k = 5
    root = [1, 2, 3, 'null', 4]
    s = Solution()
    root = inputToTreeNode(root)
    print(s.kthLargestPerfectSubtree(root, 3))
