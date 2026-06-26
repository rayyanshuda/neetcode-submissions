class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # for s, make a hash map of each letter (key) to occurance of letter (value)
        # for t, go through each letter
        # find its letter in the s hash map and subtract 1 from the occurance
        # at the end all the values should be 0 -> return True
        # if not -> return False
        sCount = Counter(s)
        tCount = Counter(t)
        return sCount == tCount