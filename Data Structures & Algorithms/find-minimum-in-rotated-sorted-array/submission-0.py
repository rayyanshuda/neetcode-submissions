class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        while left < right:
            if nums[mid] > nums[right]:
                left = mid + 1
                mid = (left + right) // 2
            elif nums[mid] < nums[right]:
                right = mid
                mid = (left + right) // 2
        return nums[mid]