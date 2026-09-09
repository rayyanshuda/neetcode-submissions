class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # have an index at the end of the list
        # have an index at the start
        # if the start index is val
        # swap with end index
        # move end index - 1 and start index + 1
        end = len(nums) - 1
        start = 0
        while start < end:
            if nums[start] == val:
                while start < end and nums[start] == val and nums[end] == val:
                    end -= 1
                if start < end:
                    nums[start], nums[end] = nums[end], nums[start]
                    end -= 1
                else:
                    break  # All remaining are vals, stop
            start += 1
        
        # Check if final position is a non-val
        if start == end and nums[start] != val:
            start += 1
    
        return start
            
        