class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store_dict = {}

        for i in range(len(nums)):
            another_number = target - nums[i]

            if another_number in store_dict:
                return [store_dict[another_number], i]
            store_dict[nums[i]] = i