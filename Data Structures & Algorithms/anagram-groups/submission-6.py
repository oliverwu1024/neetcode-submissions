from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        for i in strs:
            store["".join(sorted(i))].append(i)
        return [x for x in store.values()]