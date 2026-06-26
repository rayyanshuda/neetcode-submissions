class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        check if the difference exists in the hash map
        if it doesn't -> add the current number to the hash map     
        ''' 
        i = 0
        dict1 = {}
        for num in nums:
            difference = target - num
            if difference in dict1:
                return [dict1.get(difference), i]
            dict1[num] = i
            i += 1
        
            

        