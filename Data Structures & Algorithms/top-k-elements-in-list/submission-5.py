from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = Counter(nums)
        return [x for x, y in store.most_common(k)]