class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=s.split()
        reverse_s=' '.join(words[::-1])
        return reverse_s
        