class Solution(object):
    def maxArea(self, height):
        largest=0
        n=len(height)
        left=0
        right=n-1
        while left<right:
                area=(right-left)*min(height[left],height[right])
                largest=max(largest,area)                
                if height[left]<height[right]:
                    left+=1
                else:
                    right-=1
        return largest

        return largest
        