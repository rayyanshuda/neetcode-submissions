class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        char_set = set()
        max_length = 0
        while right < len(s):
            if s[right] in char_set:
                while s[right] in char_set:
                    char_set.remove(s[left])
                    left += 1
            char_set.add(s[right])
            #max_length += 1

            current_size = right - left + 1
            max_length = max(max_length, current_size)

            right += 1
        return max_length