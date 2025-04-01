class Solution(object):
    #39 可重复选元素的组合
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans=[]
        item=[]
        n=len(candidates)
        def backtrack(i,target):
            if target==0:
                ans.append(item[:])
                return
            for j in range(i,n):
                #循环中剪枝
                if candidates[j]>target:
                    continue
                item.append(candidates[j])
                target-=candidates[j]
                #由于每个元素可以重复选，所以这里不是j+1
                backtrack(j,target)
                item.pop()
                target+=candidates[j]
        backtrack(0,target)
        return ans

    #40 含重复元素的排列，剪枝保证结果集中没有重复的items
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        #首先对candidates排序
        candidates.sort()
        ans = []
        item=[]
        n=len(candidates)
        def dfs(i,target):
            if target==0:
                ans.append(item[:])
                return
            for j in range(i, n):
                if candidates[j] > target:
                    continue
                # 最重要的剪枝，避免结果重复
                if j>i and candidates[j] == candidates[j -1]:
                    continue
                target-=candidates[j]
                item.append(candidates[j])
                dfs(j+1,target)
                item.pop()
                target+=candidates[j]
        dfs(0,target)
        return ans

    #90 全子集与组合的区别在于，组合是n个里面取k个，要求items的长度必须是k，而子集大小是任意的
    # 所以写法上有两个区别
    # 1.进入backtrack之后直接append(items)，而不是在if i==n里面append
    # 2.递归出口是i==n,并且直接return
    #此题还涉及到去重，不用效率低下的if items in ans，而是将nums排序后在for循环中做判断，和组合中的去重一模一样
    def subsetsWithDup(self, nums):
        ans, items = [], []
        n = len(nums)
        #去重要点一，必须把nums排序
        nums.sort()

        def backtrack(i):
            #与组合唯一的不同点
            ans.append(items[:])
            if i == n:
                return
            for j in range(i, n):
                #去重判断
                if j > i and nums[j] == nums[j - 1]:
                    continue
                items.append(nums[j])
                backtrack(j + 1)
                items.pop()

        backtrack(0)
        return ans

    #491 当不能改变nums顺序时，对子集的剪枝
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        ans,items=[],[]
        n=len(nums)

        def dfs(i):
            if len(items) >= 2:
                ans.append(items[:])
            if i==n:
                return
            # 仅仅在for循环中不能用用过的数，所以不能设置为全局变量
            # 因为num的取值范围是[-100,100]，所以visit大小设置为201
            visit = [False] * 201
            for j in range(i,n):
                #因为不能对nums排序，所以不能再用这个剪枝手段了
                # if j>i and nums[j]==nums[j-1]:
                #     continue
                if len(items)>0 and nums[j]<items[-1] or visit[nums[j]+100]:
                    continue
                visit[nums[j]+100]=True
                items.append(nums[j])
                dfs(j+1)
                items.pop()
                #visit在里面，不是全局的，所以不用设置回去
                # visit[nums[j] + 100] = False
        dfs(0)
        return ans


    # 46，47 全排列（含或不含重复元素均可），核心思想在于使用verdict数组判断元素是否已使用
    #除了verdict，和组合的另一个区别在于for循环是for j in range(n)而不是for j in range(i,n)
    #除此之外，由于是用if len(item) == n作为出口条件，所以backtrack不用参数了
    # 以[1,2,3]为例,如果使用暴力法，会出现[1,1,1]的情况，复杂度为n^n，而回溯法的复杂度是全排列的数量，为n!。有n!个backtrack，每个里面for循环n次，故总的复杂度是O(n*n!)
    #除此之外，此题效率最高的写法是用递归
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        item = []
        n = len(nums)
        # 利用verdict判断该元素是否使用过，用0，1也行，因为python的int和bool型大小一样
        verdict = [False] * n
        nums.sort()
        def backtrack():
            if len(item) == n:
                ans.append(item[:])
                return
            for i in range(n):
                if not verdict[i]:
                    #树层剪枝，保证这一层前面用过的数不再用
                    #当然，写不出来也可以暴力if items not in ans
                    if i>0 and nums[i]==nums[i-1] and not verdict[i-1]:
                        continue
                    item.append(nums[i])
                    verdict[i] = True
                    backtrack()
                    item.pop()
                    verdict[i] = False

        backtrack()
        return ans



if __name__ == '__main__':
    s=Solution()
    nums="23"
    print(s.letterCombinations(nums))
