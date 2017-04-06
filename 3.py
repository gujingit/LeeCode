#coding=utf-8
# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3.
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    # @return int
    def lengthOfLongestSubstring(self, s):
        size = len(s)
        subString = {}
        start = end = 0
        max = 0

        for i in range(size):
            for key in subString.keys():
                if subString[key] == s[i]:
                    for k in range(start,key+1): # if s[key] == s[i],删除start到key的所有字符
                        del subString[k]
                    start = key + 1 #更新子串start指针位置
                    break
            subString[i] = s[i]
            end = i
            if max < end - start + 1:
                max = end - start + 1 #记录最长子串值
        return max


if __name__=="__main__":
    s = Solution()
    str = 'abbaab'
    r = s.lengthOfLongestSubstring(str)
    print r

