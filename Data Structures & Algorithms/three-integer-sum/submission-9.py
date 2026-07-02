class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] ==nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums)-1

            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum ==0:
                    answer.append([nums[i], nums[left], nums[right]])
                    left +=1
                    right -=1
                    while nums[left] == nums[left-1] and left <right:
                        left+=1                


                if three_sum > 0:
                    right -=1
                if three_sum <0:
                    left+=1
        return answer

