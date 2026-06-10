class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        answer=0
        for i in range(len(nums)):
            if nums[i] == 1:
                count+=1
            answer=max(answer, count)

            if i == len(nums)-1:
                break

            if nums[i+1] == 0:
                count=0
        return answer
            