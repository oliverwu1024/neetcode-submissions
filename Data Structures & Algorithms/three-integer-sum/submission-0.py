class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # ← sort first!
        output = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # skip duplicate i
                continue
            
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    output.append([nums[i], nums[j], nums[k]])
                    # skip duplicates for j and k
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1  # ← move pointers!
                    k -= 1
                elif total < 0:
                    j += 1  # ← need a bigger number
                else:
                    k -= 1  # ← need a smaller number
        
        return output