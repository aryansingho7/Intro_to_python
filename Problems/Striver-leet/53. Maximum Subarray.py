class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        partialSum=nums[0]
        globalmax=nums[0]
        
        for i in range(1,len(nums)):
            partialSum=max(nums[i], partialSum+nums[i])
            globalmax=max(partialSum,globalmax)
        return globalmax
    