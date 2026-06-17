from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            answer = prod(nums[:i]) * prod(nums[i+1:])
            output.append(answer)
        return output