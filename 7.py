#coding=utf-8
# Reverse digits of an integer.
# Example1: x = 123, return 321
# Example2: x = -123, return -321

class Solution(object):
    #@return int
    def reverse(self, x):
        minus = 1
        r = i= 0
        if x<0:
            minus = -1
            x = x*(-1)
        while x/10 != 0:
            r = (r + x%10)*10
            x = x/10
        result = (r+x)*minus
        if result>2147483647 : return 0
        elif result < -2147483648 :return 0
        else:return (r+x)*minus

if __name__=="__main__":
    s = Solution()
    a = 1534236469
    r = s.reverse(a)
    print r

