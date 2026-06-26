import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        # number : count
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        max_heap = []
        for num in seen:
            if num in max_heap:
                continue
            else:
                heapq.heappush(max_heap, [seen[num], num])
        

        largest = heapq.nlargest(k, max_heap, key=lambda x: x[0])
        result = []
        for pair in largest:
            freq = pair[0]
            num = pair[1]
            result.append(num)
        return result



            
