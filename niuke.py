import io
import sys

# 创建一个StringIO对象，模拟输入
input_data = ("8 1 3 7\n"
              "3 1 3 1 3 2 2 3\n")
sys.stdin = io.StringIO(input_data)

def max_score(n, a, b, c, colors):
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        # Single brick elimination
        dp[i] = max(dp[i], dp[i - 1] + a)

        # Two consecutive bricks with the same color
        if i >= 2 and colors[i - 1] == colors[i - 2]:
            dp[i] = max(dp[i], dp[i - 2] + b)

        # Three consecutive bricks with the same color
        if i >= 3 and colors[i - 1] == colors[i - 2] == colors[i - 3]:
            dp[i] = max(dp[i], dp[i - 3] + c)

    return dp[n]

if __name__ == "__main__":
    # 输入
    n, a, b, c = map(int, input().split())
    colors = list(map(int, input().split()))

    # 计算最高得分
    result = max_score(n, a, b, c, colors)

    # 输出结果
    print(result)






