class Solution(object):
    def getWinner(self, arr, k):
        n = len(arr)
        if k >= n:
            return max(arr)
        champ = arr[0]
        win_count = 0
        for i in range(1, n):
            if champ > arr[i]:
                win_count += 1
            else:
                champ = arr[i]
                win_count = 1
            if win_count == k:
                return champ
        
        return champ
