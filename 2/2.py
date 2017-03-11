#coding=utf-8


class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

    def printResult(self):
        while self:
            print self.val,' ',
            self = self.next
        print ' '

class Solution(object):
    # @return a ListNode
    def addTowNumbers(self,l1,l2):
       root = n = ListNode(0)
       carry = 0
       while l1 or l2 or carry:
           v1 = v2 = 0
           if l1:
               v1 = l1.val
               l1 = l1.next
           if l2:
               v2 = l2.val
               l2 = l2.next
           carry,val = divmod(v1+v2+carry,10)
           n.next = ListNode(val)
           n = n.next
       return root.next

if __name__=="__main__":
    l1 = ListNode(0)
    l2 = l1.next = ListNode(0)
    l3 = l2.next = ListNode(5)
    l1.printResult()
    s = Solution()
    r = s.addTowNumbers(l1,l1)
    r.printResult()




