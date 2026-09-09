class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # just the array nums twice is ans
        # create array and copy nums, when reach end of nums 
        # go back to beginning
        ans = []
        restart = 0
        pointer1 = 0
        # loop 2 passes
        while restart < 2:
            ans.append(nums[pointer1])
            pointer1 += 1
            
            # check if at end
            if pointer1 == len(nums):
                restart += 1   # complete one pass
                pointer1 = 0   # go back to start
                
        return ans