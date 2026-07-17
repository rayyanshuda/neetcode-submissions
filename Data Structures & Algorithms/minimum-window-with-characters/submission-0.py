class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        countT = Counter(t)
        need = len(countT)
        have = 0
        window = {}
        left = 0
        result = [-1, -1]  # store best (left, right) found
        result_len = float("inf")
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            # if char is in countT and window[char] just reached exactly countT[char], 
            if s[right] in countT and (window[s[right]] == countT[s[right]]):
                # have += 1
                have += 1

            while have == need:
                # this window is valid - record it if it's shorter than result_len
                if (right - left + 1) < result_len:
                    result_len = right - left + 1
                    result = [left, right]

                # try to shrink - remove s[left] from window
                window[s[left]] -= 1

                # if that char was in countT and window[s[left]] just dropped below countT[s[left]]
                # have -= 1
                if s[left] in countT and (window[s[left]] < countT[s[left]]):
                    have -= 1

                left += 1

        return s[result[0]:result[1]+1] if result_len != float("inf") else ""


