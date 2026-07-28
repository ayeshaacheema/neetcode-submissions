class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #first define variables
        min_price_so_far = prices[0]
        max_profit = 0

        #initate a loop that will start from index 1 till length of prices array
        for i in range (1, len(prices)):
            #calculate profit which is selling minus buying
            profit = prices[i] - min_price_so_far
            if profit > max_profit:
                max_profit = profit
            if prices[i] < min_price_so_far:
                min_price_so_far = prices[i]
        return max_profit 
        