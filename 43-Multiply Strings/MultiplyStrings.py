#coding=utf-8


class Solution(object):
    # @return string
    def strMultiply(self,num1,num2):
        l1 = len(num1)-1
        carry = 0
        result = ''
        if int(num2)==0 or int(num1)==0: return 0
        while l1>=0 or carry:
            v1 = 0
            if l1>=0:
                v1 = int(num1[l1])
                l1 = l1-1
            carry,val = divmod(v1*int(num2)+carry,10)
            result = str(val)+result
        return result

    def strAdd(self,num1,num2):
        l1 = len(num1)
        l2 = len(num2)
        result = ''
        carry = 0
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                l1 = l1 - 1
                v1 = int(num1[l1])
            if l2:
                l2 = l2 - 1
                v2 = int(num2[l2])
            carry, val = divmod(v1 + v2 + carry, 10)
            result = str(val) + result
        return result


    def multiply(self, num1, num2):
        n = l2 = len(num2)-1
        sum = '0'
        while l2>=0:
            sumNum2 = str(self.strMultiply(num1,num2[l2]))+'0'*(n-l2)
            sum = self.strAdd(sum,sumNum2)
            l2 = l2 - 1
        if set(sum) == set('0'): sum = '0'
        return sum


if __name__=="__main__":
    str1 = '123'
    str2 = '1'
    s = Solution()
    result = s.multiply('3','52')
    print result

