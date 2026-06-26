class Solution:
    def trap(self, height: List[int]) -> int:
        # go through every single index (from start to len(height) -2. 
        # for each index find the tallest height to its left and right
        # calculate the water_level at i = min(max_left, max_right) 
        # water trapped at i = max(0, water_level - height[i]) where height[i] is the current height of the index bar. 
        # add that number to the total water trapped 
        left = 0
        right = len(height) - 1
        max_left = 0
        max_right = 0
        total_water = 0

        while left < right:
            
            if height[left] < height[right]:
                # Process left side (left side is the bottleneck)
                
                if height[left] >= max_left:
                    # Current bar is taller, update max_left
                    max_left = height[left]
                else:
                    # Current bar is shorter, water can be trapped
                    total_water += (max_left - height[left])
                
                left += 1  # Move left pointer inward
            
            else:
                # Process right side (right side is the bottleneck)

                if height[right] >= max_right:
                    # Current bar is taller, update max_right
                    max_right = height[right]
                else:
                    # Current bar is shorter, water can be trapped
                    total_water += (max_right - height[right])
                
                right -= 1  # Move right pointer inward

        return total_water

                
