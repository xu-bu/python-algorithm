#将排好序的两个数组合并,并返回这个排好序的数组
import random
import time


def merge(leftList,rightList):
    l=r=0
    result=[]
    while l<len(leftList) and r<len(rightList):
        if leftList[l]<rightList[r]:
            result.append(leftList[l])
            l+=1
        else:
            result.append(rightList[r])
            r += 1
    for each in rightList[r:]:
        result.append(each)
    for each in leftList[l:]:
        result.append(each)
    return result

#主函数只有两个部分，首先写递归出口，如果没有return，就把数组分成左右两块，分别把这两块排好序然后合并
def mergeSort(nums):
    if len(nums)<=1:
        return nums
    else:
        mid=len(nums)//2
        #将数组分成两块，分别排好序，然后拼起来
        leftList=mergeSort(nums[:mid])
        rightList=mergeSort(nums[mid:])
        return merge(leftList,rightList)


#随机选出一个下标random_index，然后将nums[random_index]和nums[left]交换，从left+1开始遍历一遍数组，完成遍历时使得比pivot=nums[left]小的数都在它左边，比它大的数都在它右边，最后返回pivot的下标
def partition(nums, left, right):
    random_index = random.randint(left, right)
    nums[random_index], nums[left] = nums[left], nums[random_index]
    pivot = nums[left]
    slow = left
    for fast in range(left + 1, right + 1):
        if nums[fast] < pivot:  # 小于pivot的元素都被交换到前面
            slow += 1
            nums[fast], nums[slow] = nums[slow], nums[fast]
    #把pivot放到自己应该在的位置
    nums[left], nums[slow] = nums[slow], nums[left]
    return slow


def quickSort(arr, low, high):
    if low < high:
        # pi = partition(arr, low, high)
        pi=partition(arr,low,high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

#自顶向下，递归调整i位置的数
def downsift(nums,n,i):
    left,right=2*i+1,2*i+2
    largest=i
    #在i的子节点中找到最大的数和i交换
    #这里改成＞号就可以从大到小排序
    if left<n and nums[i]<nums[left]:
        largest=left
    if right<n and nums[largest]<nums[right]:
        largest=right
    # 如果需要交换则交换之后递归下一层
    #否则递归结束
    if largest!=i:
        nums[i],nums[largest]=nums[largest],nums[i]
        downsift(nums,n,largest)

#时间复杂度：
#建堆时间O(n)，downsift一次是O(logn)，需要调整n次，所以是O(n*logn)
def heapSort(nums):
    n=len(nums)
    #反向构建堆,这里不用是n，n//2就够了
    for i in reversed(range(n//2)):
        downsift(nums,n,i)
    #从数组尾开始，把每个数跟根节点交换，然后调整根节点
    for i in reversed(range(n)):
        nums[0],nums[i]=nums[i],nums[0]
        #注意这里是i
        downsift(nums,i,0)



n=10
# nums=[]
# for i in range(1,n):
#     nums.append(random.randint(1,i))
# startTime=time.time()
# mergeSort(nums)
# print(f"mergesort runs for {time.time()-startTime}s")
#
# nums=[]
# for i in range(1,n):
#     nums.append(random.randint(1,i))
# startTime=time.time()
# quickSort(nums,0,len(nums)-1)
# print(f"quicksort runs for {time.time()-startTime}s")

nums=[6,3,688,42,21,1]
# for i in range(1,n):
#     nums.append(random.randint(1,i))
startTime=time.time()
quickSort(nums,0,len(nums)-1)
print(f"sort runs for {time.time()-startTime}s")
print(nums)
