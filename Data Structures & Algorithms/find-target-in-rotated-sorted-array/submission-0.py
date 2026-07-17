class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while (left <= right):
            mid = (left + right) // 2
            if nums[mid] == target: 
                return mid
            if nums[left] <= nums[mid]:
                # that means this half is sorted
                if target >= nums[left] and target < nums[mid]:
                    #the target is between left and mid pointer -> we can throw away mid to right values
                    right = mid - 1
                else:
                    # the target is not between left and mid pointer -> we can throw away left to mid values
                    left = mid + 1
            else:
                # that means this half is sorted
                if target >= nums[mid] and target <= nums[right]:
                    # the target is between mid and right pointer -> we can throw away left to mid values
                    left = mid + 1
                else:
                    # the target is not between mid and right pointer -> we can throw away mid to right values
                    right = mid - 1
        # if the loop ends without reaching the nums[mid] == target, then it is not in the list
        return -1
                

