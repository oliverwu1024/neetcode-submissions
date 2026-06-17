class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_clean= list(sorted(set(nums)))
        print(num_clean)
        count = 1
        answer = count
        for i in range(len(num_clean)-1):
            if num_clean[i+1] == num_clean[i]+1:
                count += 1
                #print(count)
                answer=max(answer,count)
            else:
                answer = max(answer, count)
                count = 1
        return answer

