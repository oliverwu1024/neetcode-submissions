class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        insert_position = 0
        k = 0 
        for i in range(len(nums)):
            if nums[i] != val:
                nums[insert_position] = nums[i]
                insert_position += 1
                k += 1

        #for j in range(insert_position, len(nums)):
        #    nums[j] = ""
        return k