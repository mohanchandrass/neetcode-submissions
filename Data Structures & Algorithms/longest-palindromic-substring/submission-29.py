class Solution:
    def longestPalindrome(self, s: str) -> str:
        word = ""
        size = 0

        if len(s)==1:
            return s[0]

        if len(s)<=2:
            if s[0] == s[1]:
                return s[0:2]
            else:
                return s[0]

        for i in range(0,len(s)):
            left = i
            right = i
            while left>=0 and right<len(s) and s[left] == s[right]:
                if right-left+1>size:
                        size = right-left+1
                        word = s[left:right+1]
                        print(word,size)
                left-=1
                right+=1
            left = i
            right = i+1
            while left>=0 and right<len(s) and s[left] == s[right]:
                if right-left+1>size:
                        size = right-left+1
                        word = s[left:right+1]
                        print(word,size)
                left-=1
                right+=1

        return word