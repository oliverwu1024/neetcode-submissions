class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(len(arr)):
            if i == len(arr)-1:
                arr[i] = -1
                break

            replace_with = max(arr[i+1:])
            arr[i] = replace_with

        return arr