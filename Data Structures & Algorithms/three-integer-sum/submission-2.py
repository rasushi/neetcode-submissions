class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        i=0
        for i, a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            else:
                l,r=i+1,len(nums)-1
                while l<r:
                    if nums[l]+nums[r]+nums[i]>0:
                        r-=1
                    elif nums[l]+nums[r]+nums[i]<0:
                        l+=1
                    else:
                        res.append([a,nums[l],nums[r]])
                        l+=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                
        return(res)


        