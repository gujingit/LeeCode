#coding=utf-8

class Solution(object):
    # @return int
    def myAtoi(self, str):
        s = list(str.strip()) #str类型的不能直接del[s[0]],所以要转成list
        size = len(s)
        if size == 0: return 0
        sign = 1
        if s[0]=='-':
            sign = -1
        if s[0] in ['-','+']:
            del(s[0]) ##如果第一位是符号位,删除
            size -= 1
        i = 0
        ret = 0
        print 'size',size
        while i<size and s[i].isdigit():
            ret = ret * 10 + int(s[i])
            i = i+1
        ret = sign * ret
        if ret > 2**31-1: return 2**31-1
        elif ret < -2**31: return -2**31
        else: return ret

if __name__=="__main__":
    s = Solution()
    str='    010'
    r = s.myAtoi(str)
    print r


