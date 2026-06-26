class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # introduce an index i
        # go through the nums list
        # if the index i is the same as int he index for nums list
        # skip it during the product calculation
        # append the product calculation to a new list
        product = []
        i = 0
        prod = 1
        while i < len(nums):
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    prod *= nums[j]
            product.append(prod)
            prod = 1
            i += 1
        return product



        # solution 2
        # calculate product to the left of index
        # ''        ''      ''  '' right '' ''
        #multiply both products and add to list