# dfs用于寻找[0,upperBond]范围内windy数的个数，从最高位开始往低位枚举
# pos表示对第几位开始枚举，如，为1表示个位
# pre表示当前位置前面的数
# flag表示是否有限制，比如，如果上限是123，假如当前百位上已经枚举出了0，要开始枚举十位上的数字，显然十位上可以选0-9，没有限制，得到的数字都不可能大于123（是否满足windy数的要求之后再看），此时把flag置为false。而如果已经枚举出了1，则十位上的数字只能选择0-2，则必须把flag置为true
def dfsVio(pos,pre,upperBond,flag):
    #第一步，设置出口
    if pos<=0:
        return 1
    #第二步，判断限制
    if flag:
        maxNum=upperBond[pos]
    else:
        maxNum=9
    ret=0
    #第三步，枚举当前位置
    for i in range(maxNum+1):
        #第四步，判断是否满足条件（此题为windy数的条件）
        if abs(i-pre)>=2:
            ret+=dfsVio(pos-1,i,upperBond,flag and upperBond[pos]==i)
    return ret

#对上面的暴力枚举法进行优化，由于在枚举的过程中，可能出现dfs(3,2,False)这个函数被算了好几次，则可以用dp[pos][pre][flag]来记录dfs函数的结果
def solve(r):
    # 父函数初始化upperBond和dp
    #初始多加一个数保证个位上的数进来以后下标为1
    upperBond=[0]
    dp=[[[-1]*2 for j in range(len(str(r))+1)]for i in range(10)]

    #拆分上界数
    for each in str(r)[::-1]:
        upperBond.append(int(each))
    # while (r):
    #     num=r%10
    #     r//=10
    #     upperBond.append(num)
    def dfs(pos, pre, flag):
        #由于dp中要用到flag，所以要从bool转到int
        flag=int(flag)
        # 第一步，设置出口
        if pos <= 0:
            return 1
        #第二步，判断是否已经算过
        if dp[pos][pre][flag]!=-1:
            return dp[pos][pre][flag]
        # 第三步，判断限制
        if flag:
            maxNum = upperBond[pos]
        else:
            maxNum = 9
        ret = 0
        # 第四步，枚举当前位置
        for i in range(maxNum+1):
            # 第五步，判断是否满足条件（此题为windy数的条件）
            if abs(i - pre) >= 2:
                ret += dfsVio(pos - 1, i, upperBond, flag and upperBond[pos] == i)
        #第六步，记录本函数的结果
        dp[pos][pre][flag]=ret
        return ret
    print(dfs(3,-2,1))

#2260
def countDigitOne(self, n: int) -> int:
    upperBond = [0]
    for each in str(n)[::-1]:
        upperBond.append(int(each))
    # dp=[[[-1]*2 for i in range(10)]for j in range(len(str(n))+1)]
    length = len(str(n))
    dp = [[[-1] * 2 for i in range(length + 1)] for j in range((length + 1))]

    # 当第pos位之前已经排好了且有ones个1的时候，返回排完剩下位之后所有这些数含有多少个1
    def dfs(pos, ones, limit):
        # 当前这个数遍历完了，返回一共有多少个1
        if pos <= 0:
            return ones
        if dp[pos][ones][limit] != -1:
            return dp[pos][ones][limit]
        if limit:
            maxNum = upperBond[pos]
        else:
            maxNum = 9
        ret = 0
        for i in range(maxNum + 1):
            curOnes = ones
            if i == 1:
                curOnes += 1
            ret += dfs(pos - 1, curOnes, int(limit and upperBond[pos] == i))
        dp[pos][ones][limit] = ret
        return ret

    return dfs(length, 0, True)

