class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        add each letter from the first word as a hash key,
        and the value would the count of how many times that letter
        occurred
        '''
        countFreq = {}
        for letter in s:
            if letter in countFreq:
                countFreq[letter] += 1
            else:
                countFreq[letter] = 1
        for letter in t:
            if letter in countFreq:
                countFreq[letter] -= 1
            else:
                return False
        for count in countFreq.values():
            if count != 0:
                return False
        return True
