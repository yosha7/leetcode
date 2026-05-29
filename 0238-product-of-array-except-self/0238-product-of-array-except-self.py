class Solution(object):
    def productExceptSelf(self, nums):
        
        length=len(nums)
        result=[1]*length
        for i in range(1,length):
            result[i]=result[i-1]*nums[i-1]
        rightprod=1
        for i in range(length-1,-1,-1):
            result[i]=rightprod*result[i]
            rightprod=rightprod*nums[i]
        return result

        