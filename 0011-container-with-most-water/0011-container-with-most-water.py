class Solution(object):
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        ans = 0

        while l < r:
            hl, hr = height[l], height[r]

            if hl < hr:
                ans = max(ans, hl * (r - l))
                l += 1
            else:
                ans = max(ans, hr * (r - l))
                r -= 1

        return ans