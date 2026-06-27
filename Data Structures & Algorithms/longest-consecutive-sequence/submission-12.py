class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num =sorted(list(set(nums)))
        answer=count = 1
        #print(sorted(nums))
        for i in range(len(num)-1):
            #if i==len(num)-1:
                #break
            if num[i+1]==num[i]+1:
                count+=1
            else:
                count = 1
            answer= max(count, answer)
        return answer
