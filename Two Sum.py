class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            firstNum = nums[i]
            secondNum = target-firstNum
            
            if secondNum in nums and nums.index(secondNum) != i:
                return i,nums.index(secondNum)
