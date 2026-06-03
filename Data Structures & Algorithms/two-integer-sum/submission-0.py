class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i,x in enumerate(nums):
            diff= target-x
            if diff in a:
                return [a[diff],i]

            else:
                a[x]=i
