class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j=0,len(heights)-1
        max_area=[0,0,0]
        while i<j:
            a=heights[i]
            b=heights[j]
            dist=j-i
            min_v=min(a,b)
            area=min_v*dist
            if area>max_area[0]:
                max_area[0]=area
                max_area[1]=i
                max_area[2]=j
            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1
        return max_area[0]
            

        