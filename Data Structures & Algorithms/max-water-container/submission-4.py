class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        mostWater = 0
        right = len(heights) - 1
        while left < right:
            container_height = min(heights[left], heights[right])
            distance = right - left
            currContainer = container_height * distance
            if currContainer > mostWater:
                mostWater = currContainer
            if heights[left] < heights[right]:
                left += 1
            elif heights[right] <= heights[left]:
                right -= 1

        return mostWater