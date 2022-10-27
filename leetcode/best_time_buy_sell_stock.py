# Leetcode problem no 121. Best time to buy and sell stock

class Solution:
    def maxProfit(self, prices:list[int]) -> int:
        buy = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if buy > prices[i]:
                buy = prices[i]
            if profit < prices[i] - buy:
                profit = prices[i] - buy
        
        return profit

def main():
    # prices = [7,1,5,3,6,4]
    prices = [7, 6, 4, 3, 1]
    solve = Solution()
    print(solve.maxProfit(prices=prices))

if __name__ == "__main__":
    main()