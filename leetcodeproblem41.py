class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while nums[i] != i+1:
                if nums[i]<=0 or nums[i]>len(nums) or nums[i]==nums[nums[i]-1]:
                    break
                else:
                    temp=nums[nums[i]-1]
                    nums[nums[i]-1]=nums[i]
                    nums[i]=temp
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1

b=Solution()
print b.firstMissingPositive([1,1])