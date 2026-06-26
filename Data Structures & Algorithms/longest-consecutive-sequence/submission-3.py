class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consecutive = set(nums)
        print(consecutive)
        longest = 0
        current_num = 0
        for num in consecutive:
            if num-1 in consecutive:
                continue
            else:
                length = 1
                current_num = num+1
                while current_num in consecutive:
                    length += 1
                    current_num += 1
                if length > longest:
                    longest = length
            
        return longest