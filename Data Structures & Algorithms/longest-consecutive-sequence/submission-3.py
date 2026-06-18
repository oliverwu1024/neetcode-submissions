class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = list(sorted(set(nums)))
        print(nums)
        count = 1
        answer = count
        for i in range(len(nums)-1):
        
            if nums[i+1] == nums[i] + 1:
                count += 1
                answer = max(answer, count)
            else:
                count = 1
                #answer= max(answer, count)
        
        return answer



