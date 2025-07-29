import bisect

# 降序数组中二分查找指定数的index
# 用法示例：index=binSearch(array,0,len(array)-1,key=lambda x:-x)
def binSearch(MountainArray, l, r, target, key=lambda x: x):
    target=key(target)
    while l <= r:
        mid = (l + r) // 2
        res = key(MountainArray[mid])
        if res == target:
            return mid
        elif mid < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

# 查找递增数组中最接近指定数的数
def getClose(arr, target):
    index = bisect.bisect_left(arr, target)
    if index == 0:
        return arr[0]
    if index == len(arr):
        return arr[-1]
    return arr[index] if abs(target - arr[index]) < abs(target - arr[index - 1]) else arr[index - 1]

if __name__ == '__main__':
    nums=[1,5,7,89,123]
    print(binSearchIter(nums,5))