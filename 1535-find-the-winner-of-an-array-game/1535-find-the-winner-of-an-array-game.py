class Solution(object):
    def getWinner(self, arr, k):
        n = len(arr)
        
        # If k >= n, maximum element will definitely win
        if k >= n:
            return max(arr)
        
        champion = arr[0]
        win_count = 0
        
        for i in range(1, n):
            if champion > arr[i]:
                win_count += 1
            else:
                champion = arr[i]
                win_count = 1
            
            if win_count == k:
                return champion
        
        return champion
