class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {} # dictionary
        for i, num in enumerate(nums):
            y = target - num
            if y in diff:
                return [diff.get(y), i]
            diff[num] = nums.index(num)