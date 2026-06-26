class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # start from the beginning
        # first element is the smallest by default
        # move through the array and find a smaller element
        # if you find a smaller value, set that value as the lowest
        # as you move, if the element is larger, calculate the profit (current element - lowest)
        # if the profit is more than the previous profit (variable to keep track of maxProfit)
        # then change profit value
        # return profit
        lowest = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            currProfit = prices[i] - lowest
            if currProfit > profit:
                profit = currProfit
        
        return profit
