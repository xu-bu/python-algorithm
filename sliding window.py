import collections

class Solution(object):
    #209 滑动窗口基本框架
    def minSubArrayLen(self, target, nums):
        start,end=0,-1
        n=len(nums)
        #初始ans是一个不可能的答案
        ans=n+1
        mySum=0
        while end<n:
            while end<n:
                # 首先end++
                end += 1
                # 更新状态
                if end<n:
                    mySum += nums[end]
                # 更新答案
                if mySum>=target:
                    ans = min(ans, end - start + 1)
                    break
            if end==n:
                break
            while start<end:
                # 更新状态
                mySum-=nums[start]
                #start++
                start+=1
                #更新答案
                if mySum>=target:
                    ans = min(ans, end - start + 1)
                else:
                    break
        #如果返回了不可能的答案说明不存在这样的子序列
        return ans if ans!=n+1 else 0

    #3
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mySet=set()
        start,end=0,-1
        n=len(s)
        if n==0:
            return 0
        ans=0
        while end<n:
            while end<n:
                #首先end++
                end+=1
                #更新状态
                if end<n and s[end] not in mySet:
                    mySet.add(s[end])
                    #更新答案
                    ans=max(ans,end-start+1)
                else:
                    break

            if end==n:
                break
            while start<end:
                # 根据题目实际情况进行调整,此题在start<end的情况不用更新答案
                if start < end and s[start] != s[end]:
                    mySet.remove(s[start])
                    start+=1
                else:
                    start+=1
                    break
        return ans



if __name__ == '__main__':
    solution = Solution()
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 3
    print(solution.longestOnes(nums,k))