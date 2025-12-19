class Solution(object):
    def maxProduct(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max,curr_min,res=arr[0],arr[0],arr[0]
        for i in range(1,len(arr)):
            temp_max=max(curr_max*arr[i],curr_min*arr[i],arr[i])
            temp_min=min(curr_max*arr[i],curr_min*arr[i],arr[i])
            res=max(temp_max,res)
            curr_max,curr_min=temp_max,temp_min
        return res