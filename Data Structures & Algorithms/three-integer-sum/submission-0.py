class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. Sort the array
        # 2. For i from 0 to len(nums)-2:
            # a. Skip duplicates for nums[i]
            # b. Set target = -nums[i]
            # c. Use two pointers to find pairs that sum to target
            # (in the portion AFTER index i)
        
        nums = sorted(nums)
        solution = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[left] + nums[right]
                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    solution.append([nums[i], nums[left], nums[right]])
                    left += 1   # move both pointers to continue searching
                    right -= 1
                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    
                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
            
        return solution
