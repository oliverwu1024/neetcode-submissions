from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store_dict = defaultdict(list)

        for s in strs:
            store_dict["".join(sorted(s))].append(s)


        return [x for x in store_dict.values()]
    