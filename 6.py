#coding=utf-8
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
#convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
#锯齿形
# PAYPALISHRING
# 1       7               13
# 2     6   8          12    14
# 3  5        9     11
# 4             10
class Solution(object):
    #@return str
    def convert(self, s, numRows):
        if numRows == 1: return s
        size = len(s)
        r = ''
        index = 1
        while index <= size: #第一行与最后一行分开处理,否则会出现重复
            r += s[index-1]
            index = index+2*(numRows-1)
        for i in range(2,numRows):
            index = i
            number = 0
            while index<=size:
                if number%2==0:
                    r += s[index-1]
                    index = index+2*(numRows-i) # 第偶数个数相差2n-2i
                else:
                    r += s[index-1]
                    index = index + 2 * i -2 # 第奇数个数相差2i-2
                number +=1
        index = numRows
        while index<=size:
            r += s[index-1]
            index = index + 2 * (numRows-1)
        return r


if __name__=="__main__":
    s = Solution()
    str = 'PAYPALISHIRING'
    r = s.convert(str,6)
    print r




