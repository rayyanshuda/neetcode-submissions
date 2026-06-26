class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            if tuple(sorted(word)) in seen:
                # add it to the list in values
                seen[tuple(sorted(word))].append(word)
            else:
                seen[tuple(sorted(word))] = [word]
        return list(seen.values())
