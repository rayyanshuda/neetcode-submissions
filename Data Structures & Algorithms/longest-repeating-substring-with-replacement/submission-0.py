class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window technique
        from collections import Counter
        count = Counter()
        left = 0
        right = 0
        maxFreq = 0
        max_length = 0
        while right < len(s):
            count[s[right]] += 1
            maxFreq = max(maxFreq, count[s[right]])
            
            window_size = right - left + 1
            while (window_size - maxFreq) > k:
                # shrink: remove s[left] from count, move left forward
                count[s[left]] -= 1  
                left += 1
                # window_size shrinks too — recompute it
                window_size = right - left + 1
            
            max_length = max(max_length, window_size)
            right += 1

        return max_length


        