class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsSet = set(nums)
        setLen = len(numsSet)
        numsLen = len(nums)
        if setLen < numsLen:
            return True
        if setLen == numsLen:
            return False
        else:
            return False
        
        
        