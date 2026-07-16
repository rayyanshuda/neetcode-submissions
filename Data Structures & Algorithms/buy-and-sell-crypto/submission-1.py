class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initialize left at 0 and right at 1
        # while right < len(prices)
        # if prices[right] - prices[left] > currMax
        # change the new max to the new selling value
        # then check if prices[right] < prices[left] (or i can just make a variable for prices[right] - prices[left] earlier and here i can check if its negative)
        # if it is less, than move left pointer to where right is and move right += 1
        # after loop finishes, return max
        left = 0
        right = 1
        currMax = 0
        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit > currMax:
                currMax = profit
            if profit < 0:
                left = right
            right += 1
        return currMax
