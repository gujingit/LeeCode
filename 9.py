#coding=utf-8
#Determine whether an integer is a palindrome. Do this without extra space.

class Solution(object):
    #@return bool
    def isPalindrome(self, x):
        s=[]
        result = True
        if x<0: return False
        while x/10 !=0:
            number = x%10
            s.append(number)
            x = x/10
        s.append(x%10)
        i = 0
        j = len(s)-1
        while i<=j :
            if s[i]==s[j]:
                i += 1
                j -= 1
            else:
                result = False
                break
        return result


if __name__=="__main__":
    s = Solution()
    number = -121
    r = s.isPalindrome(number)
    print r


