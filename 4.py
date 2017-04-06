#coding=utf-8

# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

class Solution(object):
    # @return float
    def median(self,nums):
        m = len(nums)
        if  m % 2 == 0:
            return (float(nums[m/2])+float(nums[m/2-1]))/2.0
        else:
            return nums[(m-1)/2]

    # 注意有nums=[] 的情况
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        if m==0:
            return self.median(nums2)
        if n==0:
            return self.median(nums1)
        i = j = mid = 0
        l = [0.0]*(m+n)
        if (m+n)%2 == 0:
            mid = (m+n)/2
        else:
            mid = (m+n-1)/2

        while i + j <= mid:
            if i >= m :
                l[i+j] = nums2[j]
                j = j+1
                continue #注意continue 与 break
            if j >= n:
                l[i+j] = nums1[i]
                i = i+1
                continue
            if nums1[i]<=nums2[j]:
                l[i+j] = nums1[i]
                i += 1
            else:
                l[i+j] = nums2[j]
                j += 1
        if (m+n)%2 != 0: return float(l[mid]) #判断还是应该用m+n,而不是mid
        else: return (float(l[mid])+float(l[mid-1]))/2.0

if __name__=="__main__":
    s = Solution()
    nums1 = [1,3]
    nums2 = [2]
    r = s.findMedianSortedArrays(nums1,nums2)
    print r


