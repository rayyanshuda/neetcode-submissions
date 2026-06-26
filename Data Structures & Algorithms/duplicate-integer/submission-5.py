class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsList = set()
        for num in nums:
            if num in numsList:
                return True
            else:
                numsList.add(num)
        return False
