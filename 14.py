#coding=utf-8

class Solution(object):
    #@return str
    def longestCommonPrefix(self, strs):
        size = len(strs)
        ret = ''
        if size == 0: return ret
        prefix = 0
        flag = True
        minSize = min([len(s) for s in strs])
        while flag and prefix<minSize:
            for i in range(1,size):
                if strs[i][prefix] != strs[0][prefix]:
                    flag = False
                    break
            if flag:
                ret += strs[0][prefix]
                prefix += 1
        return ret


if __name__=="__main__":
    s = Solution()
    strs = ['abc','abcd','bca']
    r = s.longestCommonPrefix([])
    print r
