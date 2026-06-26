class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        i = 0
        for num in nums:
            diff = target - num
            if diff not in seen:
                seen[num] = i
                i += 1
            else:
                return [seen[diff], i]