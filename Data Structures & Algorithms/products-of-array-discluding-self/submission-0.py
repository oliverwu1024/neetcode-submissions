from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            product = prod(nums[:i] + nums[i+1:])
            output.append(product)
        return output
            