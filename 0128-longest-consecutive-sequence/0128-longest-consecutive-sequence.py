class Solution(object):
    def longestConsecutive(self, nums):
        longest=0
        set_nums=set(nums)
        for num in set_nums:
            if num-1 not in set_nums:
                length=1
                while num+length in set_nums:
                    length+=1
                longest=max(longest,length)
            
        return longest




        