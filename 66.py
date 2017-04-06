#coding=utf-8


class Solution(object):
    # @reutrn List[int]
    def plusOne(self, digits):
       l = len(digits)-1
       carry,val = divmod(digits[l]+1,10)
       result = [val]
       l = l-1
       while l>=0 or carry:
           v1 = 0
           if l>=0:
               v1 = digits[l]
               l = l-1
           carry,val = divmod(v1+carry,10)
           result.insert(0,val)
       return result


if __name__=="__main__":
    l1 = [99]
    s = Solution()
    r = s.plusOne(l1)
    print r

