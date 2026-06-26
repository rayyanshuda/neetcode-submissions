from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for word in strs:
            # Sort the word to use as a key (e.g., 'eat' -> 'aet')
            key = ''.join(sorted(word))
            anagrams[key].append(word)
        
        # Return the grouped anagrams
        return list(anagrams.values())