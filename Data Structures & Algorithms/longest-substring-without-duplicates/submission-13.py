class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # while s[right] in window: remove s[left] from window, left += 1
        # add s[right] to set
        # right += 1
        seen = set()
        left = 0
        right = 0
        max_seen = 0
        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            if (right - left + 1) > max_seen:
                    max_seen = right - left + 1
            right += 1
        return max_seen
            

