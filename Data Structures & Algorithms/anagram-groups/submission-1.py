from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        store_dict =defaultdict(list) 
        
        for s in strs:
            sorted_s = "".join(sorted(s))
            store_dict[sorted_s].append(s)
        
        return list(store_dict.values())