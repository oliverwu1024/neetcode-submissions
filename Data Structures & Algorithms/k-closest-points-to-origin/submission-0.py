class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from collections import defaultdict
        store = defaultdict(list)

        # Group points by squared distance
        for x, y in points:
            dist_sq = x*x + y*y
            store[dist_sq].append([x, y])

        # Sort the distinct squared distances
        sorted_dists = sorted(store.keys())

        output = []
        for d in sorted_dists:
            for pt in store[d]:
                if len(output) == k:
                    break
                output.append(pt)
            if len(output) == k:
                break

        return output  
        

            
        