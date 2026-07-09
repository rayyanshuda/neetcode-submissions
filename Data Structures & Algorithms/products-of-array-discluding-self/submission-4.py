class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        # prefix
        i = 0
        prefix_prod = 1
        while i < len(nums):
            prefix.append(prefix_prod)
            prefix_prod *= nums[i]
            i += 1
        print(prefix)
        # suffix
        # prefix but start from right to left
        j = len(nums) - 1
        suffix_prod = 1
        while j > -1:
            suffix.append(suffix_prod)
            suffix_prod *= nums[j]
            j -= 1
        # reverse list?
        suffix.reverse()
        print(suffix)
        # multiply suffix and prefix index and return List
        prod = []
        j = 0
        while j < len(prefix):
            prod.append(prefix[j] * suffix[j])
            j += 1
        return prod
        
