class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        answer = 0

        for i in range(len(heights)):

            left = i
            right = len(heights) - 1

            while left <right:
                if heights[left] <heights[right]:
                    area =(right-left)* heights[left]
                    answer = max(area, answer)
                    left+=1
                else:
                    area =(right-left)* heights[right]
                    answer = max(area, answer)
                    right -= 1
        
        return answer

        