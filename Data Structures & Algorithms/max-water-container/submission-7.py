class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        answer = 0
        while left < right:
            if heights[left] < heights[right]:
                base = right -left
                area = base * heights[left]
                answer = max(answer, area)
                left += 1
            else:
                base = right -left
                area = base * heights[right]
                answer = max(answer, area)
                right -= 1 
            #left += 1
            #right -= 1        
        return answer
