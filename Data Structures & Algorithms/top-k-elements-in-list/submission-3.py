from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_dict = Counter(nums)

        return [x for x,y in count_dict.most_common(k)]