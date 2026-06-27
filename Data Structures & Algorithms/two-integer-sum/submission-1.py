class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(nums)):
            other = target - nums[i]
            if other in store:
                return [store[other], i]
            store[nums[i]]=i 