#coding=utf-8

class Solution(object):
    # @return int
    def maxArea(self, height):
        size = len(height)
        maxArea = 0
        i = 0; j= size-1
        while i<j: #O(n)
            area = min(height[i],height[j])*(j-i)
            if area>maxArea: maxArea = area
            # 如果area2比area1大,则a2的min(height[i],height[j])一定大于a1的min
            # 即 area=min*length length减少,min增大
            if height[i]< height[j]: i += 1
            if area>maxArea: maxArea = area
            else: j -= 1
        return maxArea

if __name__=="__main__":
    s = Solution()
    height=[1,2,3,4,5,6,7]
    r = s.maxArea(height)
    print r