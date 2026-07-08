class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anagrams = defaultdict(list)
        for word in strs:
            # must go through every word -> minimum will be O(n)
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word].append(word)
        return list(anagrams.values())
