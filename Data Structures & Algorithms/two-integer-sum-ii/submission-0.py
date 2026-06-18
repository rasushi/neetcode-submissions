class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a={}
        for i in range(len(numbers)):
            diff=target-numbers[i]
            if diff in a:
                return([a[diff],i+1])
            else:
                a[numbers[i]]=i+1
        