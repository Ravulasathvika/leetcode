class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        D_val=len(s)
        I_val=0
        l1=[]
        
        for i in s:
            if i=='I':
                l1.append(I_val)
                I_val+=1
            else:
                l1.append(D_val)
                D_val-=1
        l1.append(I_val)
        return l1
                