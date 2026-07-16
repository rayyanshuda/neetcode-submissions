class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        no_dups = []
        max_length = 0
        length = 0
        for char in s:
            if char in no_dups:
                del no_dups[:no_dups.index(char) + 1]
                length = len(no_dups)
            length += 1
            no_dups.append(char)
            if length > max_length:
                    max_length = length
        print(no_dups)
        return max_length

