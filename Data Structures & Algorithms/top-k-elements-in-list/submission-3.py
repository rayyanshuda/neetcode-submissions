class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        freq = Counter(nums)
        # freq gives num:frequency -> need just num
        elements = [element for element, frequency in freq.most_common(k)]
        return elements