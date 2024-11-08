class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=s.split()
        n=len(words)
        for i in range(n):
            words[i]=words[i][::-1]
        s=' '.join(words)
        return s
        