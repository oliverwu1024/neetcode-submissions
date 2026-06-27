from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            output = prod(nums[:i]) * prod(nums[i+1:])
            answer.append(output)
        return answer