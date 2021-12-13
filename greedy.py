
class Solution(object):
    #53
    # 当前“连续和”为负数的时候立刻放弃，从下一个元素重新计算“连续和”，因为负数加上下一个元素 “连续和”只会越来越小。
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        i=0
        #预处理，去掉首尾的负数
        while i<n:
            if nums[i]>=0:
                break
            i+=1
        j=n-1
        while j>=0:
            if nums[j]>=0:
                break
            j-=1

        def process(nums):
            n=len(nums)
            ans = nums[0]
            mySum = 0
            for i in range(n):
                mySum += nums[i]
                if mySum < 0:
                    return max(ans, self.maxSubArray(nums[i+1:]))
                ans=max(ans,mySum)
            return ans
        if i>j:
            return max(nums)
        return process(nums[i:j+1])


if __name__ == '__main__':
    solution=Solution()
    s = "101023"
    nums = [5,4,-1,7,8]
    k = 1
    print(solution.maxSubArray(nums))