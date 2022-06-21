def minimum_coin(coins, amount):
    dp = [amount+1]*(amount+1)
    dp[0] = 0

    for a in range(1, amount+1):
        for c in coins:
            if a-c >= 0:
                dp[a] = min(dp[a], 1+dp[a-c])
    return dp[amount] if dp[amount] != amount+1 else -1

if __name__ == "__main__":
    print(minimum_coin([1,3,4], 7))