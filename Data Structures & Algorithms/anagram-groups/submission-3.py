from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        storedict = defaultdict(list)
        for i in strs:
            storedict["".join(sorted(i))].append(i)
        
        return [x for x in storedict.values()]