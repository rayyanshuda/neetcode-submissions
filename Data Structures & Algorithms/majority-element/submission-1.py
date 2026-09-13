class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # sort the list
        # for every similar element
        # we move the count up by one
        # if the next element is different
        # check if current count is higher than most count and swap if it is and also change the mostFrequentElement
        # return the number with the highest count
        nums.sort()
        
        mostCount = 0
        freqElement = 0
        
        i = 0
        while i < len(nums):
            currCount = 1
            currElement = nums[i]
            
            # Count consecutive equal elements
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                currCount += 1
                i += 1
            
            # Check if this is the most frequent so far
            if currCount > mostCount:
                mostCount = currCount
                freqElement = currElement
            
            i += 1
        
        return freqElement




