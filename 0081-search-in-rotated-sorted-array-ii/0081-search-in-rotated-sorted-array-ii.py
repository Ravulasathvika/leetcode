class Solution(object):
    def search(self, arr, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left,right=0,len(arr)-1
        while left<=right:
            mid=(left+right)//2
            if arr[mid]==target:
                return True
            if arr[left]==arr[mid]:
                left+=1
                continue
            if arr[left]<=arr[mid]:
                if arr[left]<=target<arr[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if arr[mid]<target<=arr[right]:
                    left=mid+1
                else:
                    right=right-1
        return False
