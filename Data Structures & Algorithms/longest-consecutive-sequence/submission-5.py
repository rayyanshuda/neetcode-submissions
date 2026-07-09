class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        curr_count = 0
        longest = 0
        for num in nums:
            if (num - 1) in nums:
                continue
            curr_count = 1
            val = num + 1
            while val in nums:
                curr_count += 1
                val += 1
            if curr_count > longest:
                longest = curr_count
        return longest