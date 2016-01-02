class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result=[]
        if len(nums)==1:
            return [str(nums[0])]
        elif len(nums)>0 :
            first=nums[0]
            last=nums[0]
            for i in range(1,len(nums)):
                if nums[i]!=(nums[i-1]+1):
                    if first==last:
                        result.append(first)   
                    else:
                        result.append(str(first)+"->"+str(last))
                    first=nums[i]
                last=nums[i]
            if first==last:
                result.append(first)   
            else:
                result.append(str(first)+"->"+str(last))
        return result

s=Solution()
print s.summaryRanges([0,1])