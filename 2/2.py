#coding=utf-8
import math

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def List2Num(self, x):
        l = [0] * 100
        num = 0
        while x.next:
            l[num] = x.val
            num += 1
            x = x.next
        l[num] = x.val
        result = 0
        for i in xrange(num):
            result += int(l[i]) * math.pow(10,i)
        return result

    def Num2List(self,x):
        l = [0]  *100
        index = 0
        x = int(x)
        while x != 0:
            l[index] = x % 10
            x = x / 10
            index += 1
        return l[:index]

    def addTwoNumbers(self, l1, l2):
       
        a1 = self.List2Num(l1.val)
        a2 = self.List2Num(l2.val)
        r = a1 + a2
        result = self.Num2List(r)
        return ListNode(result).val



if __name__ == "__main__":
    l1 = ListNode([2,3,4])
    l2 = ListNode([4,5,3])
    s = Solution()
    r = s.addTwoNumbers(l1,l2)
    print r
