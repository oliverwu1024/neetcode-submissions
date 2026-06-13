from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        store_dict = Counter(nums)



        return [x for x, y in store_dict.most_common(k)]