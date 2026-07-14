class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0:
                if nums[i] == nums[i-1]:
                    continue
            left = i+1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < (-1 * nums[i]):
                    left += 1
                elif nums[left] + nums[right] > (-1 * nums[i]):
                    right -= 1
                else:
                    # found a match
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    right -= 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
        return triplets
