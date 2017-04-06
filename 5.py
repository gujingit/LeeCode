#coding=utf-8
#Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.

#如果需要规避奇偶问题可以通过如下方法:
# 原串：    w a a b w s w f d
# 新串:  # w # a # a # b # w # s # w # f # d #


class Solution(object):
    #@return string
    def expand(self,s,i,front,end):
        m = len(s)
        while i - front >= 0 and i + end < m and s[i - front] == s[i + end]:
            front += 1
            end += 1
        return front,end

    def longestPalindrome(self, s):
       m = len(s)
       if m<=1 : return s
       mid = max = 0
       maxF = maxE = 0
       for i in range(1,m):
           #奇回文子串
           front = end = 0
           front,end = self.expand(s,i,front,end)
           if max < end + front - 2:
               mid = i
               maxF = front - 1
               maxE = end
               max = end + front - 2

            #偶回文串
           front = 1;end = 0
           front,end = self.expand(s,i,front,end)
           if max < end + front - 2:
               mid = i
               maxF = front - 1
               maxE = end
               max = end + front - 2
       if mid-maxF==mid+maxE: return s[0] # 如果没有回文串,则返回字符串第一
       else: return s[mid-maxF:mid+maxE]


if __name__=="__main__":
    s = Solution()
    str = 'abcda'
    r = s.longestPalindrome(str)
    print r