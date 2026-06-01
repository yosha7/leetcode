class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left=0
        longest=0
        right=0
        seen=set()
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            length=right-left+1
            longest=max(longest,length)
        return longest

